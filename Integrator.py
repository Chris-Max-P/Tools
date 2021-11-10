import os
import pathlib
import datetime
import shutil
from util.helper_functions import choose_fitting_dir
from paths_and_data import *

file_list = os.listdir(stack)

for file in file_list:
    source_file = os.path.join(stack, file)
    file_stats = pathlib.Path(source_file)
    creation_time = datetime.datetime.fromtimestamp(file_stats.stat().st_ctime)

    year = creation_time.year
    target_dir_path = choose_fitting_dir(archive, str(year))

    shutil.move(source_file, target_dir_path)  # TODO rename: Beschreibung


