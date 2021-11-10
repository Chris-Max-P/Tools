import os
import pathlib


def get_year(string):
    year = string[:4]
    return year


def choose_fitting_dir(path, year):
    for dir_name in os.listdir(path):
        print(f'tar {get_year(dir_name)} vs source {year}')
        print(get_year(dir_name) == year)
        if get_year(dir_name) == year:
            return os.path.join(path, dir_name)


