import os
import shutil
from pathlib import Path

def clean_project():
    root_dir = Path(r"e:\Download\book-skill-test-bench")
    archive_dir = root_dir / "archive"
    src_dir = root_dir / "src"
    data_dir = root_dir / "data"
    
    # Create required directories
    dirs_to_create = [
        archive_dir,
        src_dir,
        data_dir / "books",
        data_dir / "ground_truth",
        data_dir / "evaluation_out",
    ]
    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)
        
    print("Created new directory structure.")

    # 1. Archive temporary files
    for f in root_dir.iterdir():
        if f.is_file():
            name = f.name
            if name.endswith('.txt') or name.startswith('temp') or name.startswith('task_') or name.startswith('scratch_') or name.startswith('extract'):
                shutil.move(str(f), str(archive_dir / name))
                print(f"Archived: {name}")

    # 2. Move core scripts to src/
    test_bench_eval = root_dir / "test-bench" / "evaluation"
    if test_bench_eval.exists():
        for f in test_bench_eval.glob("*.py"):
            shutil.move(str(f), str(src_dir / f.name))
            print(f"Moved to src/: {f.name}")
            
    scripts_dir = root_dir / "scripts"
    if scripts_dir.exists():
        for f in scripts_dir.glob("*.py"):
            shutil.move(str(f), str(src_dir / f.name))
            print(f"Moved to src/: {f.name}")

    # 3. Move ground-truth to data/ground_truth/
    test_bench_gt = root_dir / "test-bench" / "ground-truth"
    if test_bench_gt.exists():
        for item in test_bench_gt.iterdir():
            shutil.move(str(item), str(data_dir / "ground_truth" / item.name))
            print(f"Moved ground truth: {item.name}")

    # 4. Clean up old test-bench directory entirely by archiving it instead of deleting to be safe
    test_bench = root_dir / "test-bench"
    if test_bench.exists():
        shutil.move(str(test_bench), str(archive_dir / "old_test_bench"))
        print("Archived old test-bench directory.")

    print("Cleanup and restructuring complete.")

if __name__ == "__main__":
    clean_project()
