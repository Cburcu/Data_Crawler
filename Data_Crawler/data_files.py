import os
from data_crawler import data_crawler

def write_html_data_to_file(URL, soup, folder_name):
    folder = 'Datas/'+folder_name
    if not os.path.exists(folder):
        print('Create project' + folder)
        os.makedirs(folder)

    data_folder = folder + '/data.txt'
    f = open(data_folder, 'a', encoding='utf-8')
    f.write(URL+'\n')

    data_crawler(f, soup)

    f.close()