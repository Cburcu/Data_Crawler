from bs4 import BeautifulSoup
from urllib.request import urlopen

class Html_Connection:
    URL = ''
    folder_name = ''
    data_folder_name = ''

    def __init__(self, url, folder_name):
        Html_Connection.URL = url
        Html_Connection.folder_name = 'Models/'+folder_name
        Html_Connection.data_folder_name = folder_name + '/data.txt'


    @staticmethod
    def read_html():
        ### Read HTML
        try:
            html = urlopen(Html_Connection.URL).read()
            soup = BeautifulSoup(html, 'html.parser')
        except:
            print('URL can not read!!!')
        return soup
