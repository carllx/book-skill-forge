import json

with open('E:/Download/book-skill-test-bench/.agent/skills/art_visual_guide/.agent_tasks/task_3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

prompt = data['prompt']
context = data['context']
output_file = data['output_file']

with open('E:/Download/book-skill-test-bench/.agent/skills/art_visual_guide/.agent_tasks/task_3_prompt.txt', 'w', encoding='utf-8') as f:
    f.write(prompt)

with open('E:/Download/book-skill-test-bench/.agent/skills/art_visual_guide/.agent_tasks/task_3_context.txt', 'w', encoding='utf-8') as f:
    f.write(context)

with open('E:/Download/book-skill-test-bench/.agent/skills/art_visual_guide/.agent_tasks/task_3_output_file.txt', 'w', encoding='utf-8') as f:
    f.write(output_file)
