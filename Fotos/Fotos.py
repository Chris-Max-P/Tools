import os
import os.path
import time
import shutil
from datetime import datetime
import exifread
from paths_and_data import *

def extract_creation_date(file):
    #cr_date = datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y")
    #cr_date = Image.open(file).getexif()[36867] # from PIL import Image
    with open(file, 'rb') as image:
        cr_date_obj = exifread.process_file(image, stop_tag="EXIF DateTimeOriginal")["EXIF DateTimeOriginal"]
    cr_date = datetime.strptime(str(cr_date_obj), "%Y:%m:%d %H:%M:%S")
    return cr_date


def sort_media_by_date(source_dir, base_media_folder):
    for item in os.listdir(source_dir):
        date = extract_creation_date(os.path.join(source_dir, item))
        date_str = date.__str__().split(' ')[0]
        time_str = date.__str__().split(' ')[1].replace(':', '-')

        file_name, file_extension = os.path.splitext(item)
        year_dir = os.path.join(mein_leben, str(date.year) + f' ({str(date.year - 1993)})')
        day_dir = os.path.join(base_media_folder, year_dir, date_str)

        if not os.path.exists(year_dir):
            os.mkdir(year_dir)
        if not os.path.exists(day_dir):
            os.mkdir(day_dir)

        # move file
        target_dir = os.path.join(base_media_folder, year_dir, date_str, f'{time_str}_{item}') # TODO file name not unique
        shutil.move(os.path.join(source_dir, item), target_dir)


sort_media_by_date(source_dir, mein_leben)


# TODO Veranstaltungen aus Kalender auslesen und Ordner entsprechend bennen + zusammenfassen






