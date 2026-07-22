import json
import sys

def merge(in1, in2, out):
    try:
        d1 = json.load(open(in1, encoding='utf8'))
        d2 = json.load(open(in2, encoding='utf8'))
        d1['mappings'].extend(d2.get('mappings', []))
        d1['extracted_concepts'].extend(d2.get('extracted_concepts', []))
        json.dump(d1, open(out, 'w', encoding='utf8'))
    except Exception as e:
        print(f"Merge error: {e}")

if len(sys.argv) == 4:
    merge(sys.argv[1], sys.argv[2], sys.argv[3])
