
import os
from read_directory import link_data
from cleaners.arabalar_cleaner import arabalar_cleaner
from cleaners.donanimhaber_cleaner import donanimhaber_cleaner
from cleaners.otoclub_cleaner import otoclub_cleaner
from cleaners.shiftdelete_cleaner import shiftdelete_cleaner
from cleaners.otopark_cleaner import otopark_cleaner

PATHS = link_data('Bad_Data')

for PATH in PATHS:
    file = open(PATH, mode='r', encoding='utf8')
    file_name = PATH.split('/')[1]
    file_write_path = 'Clean_Data/' + file_name + '/clean_data.txt'
    dirname = os.path.dirname(file_write_path)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    file_write = open(file_write_path, mode='a', encoding='utf8')
    text = file.readlines()

    if 'ARABALAR' in PATH:
        arabalar_cleaner(text, file_write)
    elif 'DONANIMHABER' in PATH:
        donanimhaber_cleaner(text, file_write)
    elif 'OTOCLUBTURKIYE' in PATH:
        otoclub_cleaner(text, file_write)
    elif 'SHIFTDELETE' in PATH:
        shiftdelete_cleaner(text, file_write)
    elif 'OTOPARK' in PATH:
        otopark_cleaner(text, file_write)

    file.close()
    file_write.close()