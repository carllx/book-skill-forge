import json
import os

with open('E:/Download/book-skill-test-bench/.agent/skills/modern_sculpture/.agent_tasks/qa_tasks.json', encoding='utf-8') as f:
    tasks = json.load(f)

for i, t in enumerate(tasks):
    with open(f'E:/Download/book-skill-test-bench/.agent/skills/modern_sculpture/.agent_tasks/task_{i}.json', 'w', encoding='utf-8') as out:
        json.dump(t, out, indent=2, ensure_ascii=False)
print("Saved 17 tasks to task_0.json ... task_16.json")
