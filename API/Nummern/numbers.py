import os
from util.json_i_o import *


archive = "/home/pi/06 Archiv"
define_later = "numbers"
numbers_json = os.path.join(archive, define_later + ".json")

def get_number(domain, number_key):
    numbers = file_to_dict(numbers_json)
    return numbers[domain][number_key]


def set_number(domain, number_key, number):
    numbers = file_to_dict(numbers_json)

    if domain in numbers:
        numbers[domain][number_key] = number
    else:
        numbers[domain] = {number_key: number}

    dict_to_file(numbers_json, numbers)


def get_numbers():
    return

