from util.json_i_o import dict_to_file, file_to_dict
from paths_and_data import *


books_dict: dict = file_to_dict(books_file)


def dict_keys_to_string(dict):
    entrys = ''
    for key in dict:
        entrys += f'- {key}\n'
    return entrys


def write(category_dict):
    # new category dict
    if category_dict is None:
        new_category = input("Category unknown. Want to create? y/n\n")
        if new_category == 'y':
            category_dict = {}
            books_dict[category] = category_dict
        elif new_category == 'n':
            return

    # new title dict
    title, rating, content = input("'<Title>, <Rating>, <Content>' pls\n").split(',')
    book_dict = {
        "rating": rating,
        "content": content
    }
    category_dict[title] = book_dict

    dict_to_file(books_file, books_dict)


def read(category_dict):
    for key in category_dict:
        print(f'{key}: {category_dict[key]["content"]}, {category_dict[key]["rating"]}/10')
    print('\n')


def remove(category_dict):
    to_remove = input("Delete entry?\n" + dict_keys_to_string(category_dict))
    category_dict.pop(to_remove)

    dict_to_file(books_file, books_dict)


action = 'start'
while action != '':
    action = input("in, out or remove?\n")
    if action == '': continue
    category = input("Category?\n" + dict_keys_to_string(books_dict))

    if category in books_dict:
        category_dict = books_dict[category]
    else:
        category_dict = None

    if action == 'out' or action == 'o':
        read(category_dict)
    elif action == 'in' or action == 'i':
        write(category_dict)
    elif action == 'remove' or action == 'r':
        remove(category_dict)
    print("Job done, Sir.")


