import os
import glob

input_dir = r'e:\Download\book-skill-test-bench\data\books\language_new_media'
output_dir = r'e:\Download\book-skill-test-bench\data\books\language_new_media_chunks'

os.makedirs(output_dir, exist_ok=True)

files = sorted(glob.glob(os.path.join(input_dir, 'part_*.md')))
chunk_size = 11

count = 0
for i in range(0, len(files), chunk_size):
    chunk_files = files[i:i+chunk_size]
    chunk_content = []
    for f in chunk_files:
        with open(f, 'r', encoding='utf-8') as infile:
            chunk_content.append(infile.read())
    
    chunk_filename = os.path.join(output_dir, f'chunk_{i//chunk_size + 1:02d}.md')
    with open(chunk_filename, 'w', encoding='utf-8') as outfile:
        outfile.write('\n\n'.join(chunk_content))
    count += 1
    
print(f'Successfully created {count} chunks.')
