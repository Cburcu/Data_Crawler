import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from read_file import read_brand_list
from data_crawler import data_crawler
from read_directory import link_data

PATHS = link_data('Links')

for PATH in PATHS:
    brands_lines = read_brand_list(PATH)
    DOMAIN_NAME = PATH.split('/')[1]
    FOLDER_NAME = 'Bad_Data/' + DOMAIN_NAME
    DATA_FOLDER = FOLDER_NAME + '/data.txt'

    if not os.path.exists(FOLDER_NAME):
        print('Create project' + FOLDER_NAME)
        os.makedirs(FOLDER_NAME)

    f = open(DATA_FOLDER, 'w+', encoding='utf-8')

    for line in brands_lines:
        URL = line
        if 'profil' in line:
            continue
        elif DOMAIN_NAME.lower() not in line:
            continue
        else:        
            try:
                html = urlopen(URL).read()
                soup = BeautifulSoup(html, 'html.parser')
                data_crawler(f, soup)
            except:
                print('URL can not read!!!')
                print(URL)
    f.close()   
    
    