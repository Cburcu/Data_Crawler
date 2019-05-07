from crawlers.arabalar_crawler import arabalar_crawler
from crawlers.donanimhaber_crawler import donanimhaber_crawler
from crawlers.otoclubturkiye_crawler import otoclubturkiye_crawler
from crawlers.otopark_crawler import otopark_crawler
from crawlers.shiftdelete_crawler import shiftdelete_crawler

def data_crawler(f, soup):
    if 'ARABALAR' in str(f):
        arabalar_crawler(f,soup)
    elif 'DONANIMHABER' in str(f):
        donanimhaber_crawler(f,soup)
    elif 'OTOCLUBTURKIYE' in str(f):
        otoclubturkiye_crawler(f,soup)
    elif 'OTOPARK' in str(f):
        otopark_crawler(f,soup)
    elif 'SHIFTDELETE' in str(f):
        shiftdelete_crawler(f,soup)