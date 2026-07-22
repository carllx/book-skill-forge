import os
import json
import uuid
import shutil
from pathlib import Path

class SandboxViolationError(Exception):
    pass

def get_current_sandbox_path() -> Path:
    """
    获取当前受到环境变量锁定的沙盒目录。
    """
    sandbox_path_str = os.environ.get("BSF_CURRENT_SANDBOX")
    
    if not sandbox_path_str:
        raise SandboxViolationError("【隔离沙盒红线违规】未检测到沙盒环境变量 BSF_CURRENT_SANDBOX！严禁直接写回全局目录，请由工作流调度器分配专属的时间戳沙盒。")
        
    sandbox_path = Path(sandbox_path_str)
    
    if not sandbox_path.is_dir():
        raise SandboxViolationError(f"【隔离沙盒红线违规】指定的沙盒路径 {sandbox_path} 不存在！请确保工作流正确初始化了沙盒。")
        
    return sandbox_path

def get_vendor_workspace(vendor_name: str) -> Path:
    """
    为防止并发踩踏，在当前沙盒内部为特定选手(Vendor)创建一个专属的独立画室（子目录）。
    """
    sandbox_dir = get_current_sandbox_path()
    vendor_dir = sandbox_dir / vendor_name
    vendor_dir.mkdir(parents=True, exist_ok=True)
    return vendor_dir

def enforce_sandbox_write(file_path: str):
    """
    防篡改卫士：检查即将写入的文件路径是否合法地位于当前沙盒之内。
    """
    sandbox_dir = get_current_sandbox_path()
    target_path = Path(file_path).resolve()
    
    try:
        target_path.relative_to(sandbox_dir.resolve())
    except ValueError:
        raise SandboxViolationError(f"【沙盒越界写拦截】脚本企图将文件写入 {target_path}，这超出了当前沙盒 {sandbox_dir} 的边界！这是严令禁止的。")

    print(f"[Sandbox Guard] Write permission granted for {target_path}")
    return True

def write_atomic_json(target_path: Path, data: dict):
    """
    原子化文件写入（Windows 安全道具交接）：
    解决 Windows 下的霸道文件锁问题。先生成带有 UUID 的临时碎片文件，写入完成后直接利用原子级重命名(或移动)覆盖目标文件。
    防止别的进程在写了一半时去读取报错。
    """
    enforce_sandbox_write(str(target_path))
    
    temp_path = target_path.with_name(f"{target_path.stem}_{uuid.uuid4().hex}.tmp")
    
    try:
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.flush()
            os.fsync(f.fileno()) # 强制刷入磁盘，避免缓存锁
            
        # os.replace 在 Windows 同样是原子操作，如果失败抛出异常
        os.replace(temp_path, target_path)
    except Exception as e:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)
        raise e
