import json


def dict_to_json_file(file, dict):
    with open(file, 'w') as file:
        file.write(json.dumps(dict, indent=2))


def json_file_to_dict(file):
    with open(file, 'r') as file:
        dict = json.loads(file.read())
    return dict

