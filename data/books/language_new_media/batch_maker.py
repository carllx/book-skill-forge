import os
import glob
import math

input_dir = r"e:\Download\book-skill-test-bench\data\books\language_new_media"
output_dir = r"e:\Download\book-skill-test-bench\data\books\language_new_media\batches"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files = sorted(glob.glob(os.path.join(input_dir, "part_*.md")))
batch_size = 20

for i in range(0, len(files), batch_size):
    batch_files = files[i:i+batch_size]
    batch_index = (i // batch_size) + 1
    output_file = os.path.join(output_dir, f"batch_{batch_index}.md")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for f in batch_files:
            with open(f, 'r', encoding='utf-8') as infile:
                outfile.write(f"\n\n--- Content from {os.path.basename(f)} ---\n\n")
                outfile.write(infile.read())
                
print(f"Created {math.ceil(len(files)/batch_size)} batches in {output_dir}")
