import json

def save_to_json(data, path):
    with open(path, "w") as f :
        json.dump(data, f)


def load_json(path):
    with open(path, "r") as f :
        return json.load(f)