import os
import subprocess
import sys
from pathlib import Path

# 定义供应商目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
VENDORS_DIR = PROJECT_ROOT / "lib" / "vendors"
ADAPTERS_DIR = PROJECT_ROOT / "src" / "adapters"

# 定义需要同步的开源项目列表
VENDORS = {
    "graphify": "https://github.com/Graphify-Labs/graphify.git",
    "book-to-skill": "https://github.com/virgiliojr94/book-to-skill.git",
    "cangjie-skill": "https://github.com/kangarooking/cangjie-skill.git"
}

def scan_vendor_diff(name: str, target_dir: Path, old_commit: str, new_commit: str):
    """调用差异嗅探器扫描核心组件变化"""
    scanner_script = ADAPTERS_DIR / "vendor_diff_scanner.py"
    if not scanner_script.exists():
        print(f"[WARN] 差异嗅探器未找到: {scanner_script}")
        return
        
    print(f"[*] 正在调用差异嗅探器扫描 {name} 的更新 (Commit: {old_commit[:7]} -> {new_commit[:7]})...")
    try:
        subprocess.run(
            ["python", str(scanner_script), name, str(target_dir), old_commit, new_commit],
            check=True
        )
    except subprocess.CalledProcessError:
        print(f"[ERROR] 嗅探器发现 {name} 的核心组件存在重大变更！请检查适配器兼容性。")

def sync_repo(name: str, url: str, target_dir: Path):
    """克隆或拉取最新的 git 仓库，并记录差异"""
    print(f"[*] 正在同步 {name}...")
    
    if target_dir.exists():
        if (target_dir / ".git").exists():
            # 获取拉取前的 commit hash
            try:
                old_commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=target_dir, capture_output=True, text=True, check=True).stdout.strip()
                
                # 执行 git pull
                result = subprocess.run(["git", "pull"], cwd=target_dir, capture_output=True, text=True, check=True)
                print(f"[OK] {name} 更新成功！\n{result.stdout.strip()}")
                
                new_commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=target_dir, capture_output=True, text=True, check=True).stdout.strip()
                
                # 如果代码有变动，调用嗅探器
                if old_commit != new_commit:
                    scan_vendor_diff(name, target_dir, old_commit, new_commit)
                else:
                    print(f"[-] {name} 已是最新，无变化。")
                    
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] {name} 更新失败: {e.stderr.strip()}")
        else:
            print(f"[WARN] {target_dir.name} 存在但不是 git 仓库，跳过更新。")
    else:
        print(f"[+] 正在克隆 {name}...")
        try:
            subprocess.run(["git", "clone", url, str(target_dir)], capture_output=True, text=True, check=True)
            print(f"[OK] {name} 克隆成功！(首次拉取无需比较差异)")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] {name} 克隆失败: {e.stderr.strip()}")

def main():
    print(f"=== BSF 开源组件同步与差异嗅探脚本 ===")
    print(f"目标目录: {VENDORS_DIR}\n")
    
    VENDORS_DIR.mkdir(parents=True, exist_ok=True)
    ADAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    
    for name, url in VENDORS.items():
        target = VENDORS_DIR / name
        sync_repo(name, url, target)
        print("-" * 40)
        
    print("[OK] 同步与嗅探完成！所有策展框架已就位。")

if __name__ == "__main__":
    main()
