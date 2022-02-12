import argparse
import os

from util.paths_and_data import database
from util.json_i_o import *

parser = argparse.ArgumentParser()
parser.add_argument("file_name")
args = parser.parse_args()
file_name = args.file_name
dictionary = json_file_to_dict(os.path.join(database, file_name + ".json"))

def save():
    update_entries(dictionary)
    dict_to_json_file(file_name, dictionary)

def get_all_values(nested_dictionary, indent=0):
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            print(" " * indent + key, ":")
            get_all_values(value, indent=indent + 2)
        else:
            print(" " * indent + key, ":", value)


def get_dict_struct(nested_dict):
    x = nested_dict.items()
    print(nested_dict.items()[0])


def new_entry():
    # get structure
    # new dict with same structure
    update_entries()
    return


def update_entries(dictionary):
    for key, value in dictionary.copy().items():
        if type(value) is dict and bool(value) is False:  # empty dict
            new_key, comma, new_value = input(f'\nEnter new key,value pair for {key}: \n').partition(',')
            # TODO make sure input is correct
            dictionary[new_key] = new_value
        elif type(value) is not dict and bool(value) is False:  # empty value
            dictionary[key] = input(f'\nEnter {key}: \n')
        elif type(value) is dict and bool(value) is True:
            update_entries(value)
        elif type(value) is not dict and bool(value) is True:
            pass

    return dictionary


def get_entry(dict, _key=None):
    if _key is None:
        get_all_values(dict)
    else:
        for key, value in dict.items():
            if _key in dict:
                return dict[_key]
            else:
                get_entry(value, _key=key)

# input
# analyze dict from json
# for all entrys that are no dicts:
# offer make entry

# output
# no parameter: output all
# parameter: output fitting (key, value) pair
