import json
import os

def export_json(data, file, indent=4):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)

def load_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)