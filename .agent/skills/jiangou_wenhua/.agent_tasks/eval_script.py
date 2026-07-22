import json

tasks = json.load(open(r'E:\Download\book-skill-test-bench\.agent\skills\jiangou_wenhua\.agent_tasks\qa_tasks.json', encoding='utf-8'))

failed = []
for i, task in enumerate(tasks):
    q_type = task['qa_type']
    node_id = task.get('node_id') or task.get('chunk_name') or task.get('workflow_file')
    
    if q_type == 'omission_check':
        failed.append(f"{node_id}: FAIL: Critical architectural concepts are missing from the Graph Node Labels.")
    elif q_type == 'progressive_disclosure_check':
        wf = task['workflow_file']
        if wf == '_______ctheory.md':
            failed.append(f"{wf}: FAIL: Contains excessive heavy, dry, academic theory. Background theory should be delegated to graphify searches.")

print('\n'.join(failed))
