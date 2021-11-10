import json


def dict_to_file(file, dict):
    with open(file, 'w') as file:
        file.write(json.dumps(dict))


def file_to_dict(file):
    with open(file, 'r') as file:
        dict = json.loads(file.read())
    return dict