import sys
import subprocess
import re
from pathlib import Path

# BSF 适配器隔离墙 - 差异嗅探器
# 责任：在 sync_vendors 同步外部开源库后，扫描 Diff 查找可能破坏本地 BSF 评测管线的核心变更。

SENSITIVE_FILES = [
    re.compile(r".*\.md$"),            # Prompts 和 Skills 通常存为 Markdown
    re.compile(r".*\.json$"),          # Schema 变动
    re.compile(r".*requirements.*\.txt$") # 依赖变动
]

def check_diff(repo_name, repo_dir, old_commit, new_commit):
    print(f"\n[Scanner] 正在对 {repo_name} 进行破坏性更新扫描...")
    
    # 提取差异文件列表
    try:
        diff_output = subprocess.run(
            ["git", "diff", "--name-only", old_commit, new_commit],
            cwd=repo_dir,
            capture_output=True, text=True, check=True
        ).stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[Scanner Error] Git diff 执行失败: {e}")
        return

    if not diff_output:
        return
        
    changed_files = diff_output.split('\n')
    alerts = []
    
    for file_path in changed_files:
        if any(pattern.match(file_path) for pattern in SENSITIVE_FILES):
            alerts.append(file_path)
            
    if alerts:
        print("\n" + "="*50)
        print("🚨 [CRITICAL ALERT] 发现核心文件遭到修改！")
        print("以下开源框架的核心功能（Prompt/Schema/依赖）可能已变更：")
        print(f"框架: {repo_name}")
        for alert in alerts:
            print(f"  - ⚠️ {alert}")
        print("\n请检查本项目内的适配器，确保本地复合管线 (Hybrid Pipeline) 的融合不受影响。")
        print("="*50 + "\n")
        # 返回失败代码以便调用方捕获
        sys.exit(1)
    else:
        print(f"[Scanner] {repo_name} 的更新属于安全范围，未触碰核心 Prompt 或 Schema。")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python vendor_diff_scanner.py <repo_name> <repo_dir> <old_commit> <new_commit>")
        sys.exit(1)
        
    repo_name = sys.argv[1]
    repo_dir = Path(sys.argv[2])
    old_commit = sys.argv[3]
    new_commit = sys.argv[4]
    
    check_diff(repo_name, repo_dir, old_commit, new_commit)
