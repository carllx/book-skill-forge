import os
import re

book_dir = r"e:\Download\book-skill-test-bench\data\books\language_new_media"
parts = [f for f in os.listdir(book_dir) if f.startswith('part_') and f.endswith('.md')]
parts.sort()

target_headers = [
    "Numerical Representation",
    "Modularity",
    "Automation",
    "Variability",
    "Transcoding",
    "The Myth of the Digital",
    "The Myth of Interactivity"
]

results = {header: [] for header in target_headers}
current_header = None
lines_collected = 0

for part in parts:
    with open(os.path.join(book_dir, part), 'r', encoding='utf-8') as f:
        for line in f:
            for th in target_headers:
                if th.lower() in line.lower() and ('#' in line or len(line.strip()) < 50):
                    current_header = th
                    lines_collected = 0
            
            if current_header and lines_collected < 20:
                results[current_header].append(line.strip())
                lines_collected += 1

for header, lines in results.items():
    print(f"\n=== {header} ===")
    print("\n".join(lines[:20]))
