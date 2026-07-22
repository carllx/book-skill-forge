import os
import shutil
import argparse
import sys

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
RUNS_DIR = os.path.join(DATA_DIR, 'evaluation_runs')

PIPELINES = ['cangjie_only', 'graphify_only', 'parallel_hybrid', 'serial_hybrid']

# Maps variants found in folder names to the canonical ground_truth folder names
BOOK_MAP = {
    'art_matters': 'art-matters',
    'art-matters': 'art-matters',
    'art_visual_guide': 'art_visual_guide',
    'design_real_world': 'design-for-the-real-world',
    'design-for-the-real-world': 'design-for-the-real-world',
    'envisioning-information': 'envisioning-information',
    'jiangouwenhua': 'jiangouwenhua',
    'kaogongji': 'kaogongji',
    'language_new_media': 'language-of-new-media',
    'language-of-new-media': 'language-of-new-media',
    'meixuesanbu': 'meixuesanbu',
    'modern_sculpture': 'passages-in-modern-sculpture',
    'passages-in-modern-sculpture': 'passages-in-modern-sculpture',
    'relational_aesthetics': 'relational-aesthetics',
    'relational-aesthetics': 'relational-aesthetics',
    'space_poetics': 'space_poetics',
    'tectonic_culture': 'studies-in-tectonic-culture',
    'studies-in-tectonic-culture': 'studies-in-tectonic-culture',
    'visual_display': 'visual-display',
    'visual-display': 'visual-display'
}

def migrate(dry_run=True):
    print(f"Starting migration. Dry run: {dry_run}")
    if not os.path.exists(RUNS_DIR) and not dry_run:
        os.makedirs(RUNS_DIR)

    for item in os.listdir(DATA_DIR):
        if not item.startswith('evaluation_out_'):
            continue
        
        # Skip if it is just "evaluation_out"
        if item == 'evaluation_out':
            continue

        item_path = os.path.join(DATA_DIR, item)
        if not os.path.isdir(item_path):
            continue

        # Extract book name and pipeline type
        name_part = item[len('evaluation_out_'):]
        
        pipeline_type = None
        for p in PIPELINES:
            if name_part.endswith('_' + p):
                pipeline_type = p
                book_variant = name_part[:-(len(p) + 1)]
                break
        
        if not pipeline_type:
            print(f"Warning: Could not determine pipeline type for {item}")
            continue
        
        book_canonical = BOOK_MAP.get(book_variant)
        if not book_canonical:
            # Fallback
            book_canonical = book_variant.replace('_', '-')
            print(f"Warning: Unknown book variant '{book_variant}', falling back to '{book_canonical}'")
            
        target_dir = os.path.join(RUNS_DIR, book_canonical, pipeline_type)
        
        print(f"Moving: {item} -> evaluation_runs/{book_canonical}/{pipeline_type}")
        
        if not dry_run:
            if not os.path.exists(target_dir):
                os.makedirs(os.path.dirname(target_dir), exist_ok=True)
            
            if os.path.exists(target_dir):
                print(f"  Target {target_dir} already exists, merging...")
                for root, dirs, files in os.walk(item_path):
                    rel_path = os.path.relpath(root, item_path)
                    target_root = os.path.join(target_dir, rel_path)
                    if not os.path.exists(target_root):
                        os.makedirs(target_root)
                    for f in files:
                        src_file = os.path.join(root, f)
                        dst_file = os.path.join(target_root, f)
                        if not os.path.exists(dst_file):
                            shutil.copy2(src_file, dst_file)
                        else:
                            print(f"  File {dst_file} exists, skipping.")
                # Optional: remove original after merge?
                # shutil.rmtree(item_path)
            else:
                shutil.move(item_path, target_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true', help='Execute the migration (turn off dry run)')
    args = parser.parse_args()
    
    migrate(dry_run=not args.execute)
