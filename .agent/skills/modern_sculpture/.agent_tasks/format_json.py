import json
import textwrap
with open('qa_tasks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('qa_tasks_formatted.txt', 'w', encoding='utf-8') as f:
    for i, t in enumerate(data):
        f.write(f"Task {i+1}\n")
        f.write(f"qa_type: {t.get('qa_type')}\n")
        id_val = t.get('node_id') or t.get('chunk_name') or t.get('workflow_file')
        f.write(f"ID: {id_val}\n")
        f.write(f"prompt: {t.get('prompt')}\n")
        context = t.get('context', '')
        f.write("context:\n")
        f.write(textwrap.fill(context, width=80))
        f.write("\n\n" + "="*80 + "\n\n")
