import json

def save_json(data, filename: str="default_save.json"):
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return True

def load_json(filename: str="default_save.json"):
    data = None
    with open(filename, 'r') as load_buf:
        data = json.load(load_buf)
    return data
