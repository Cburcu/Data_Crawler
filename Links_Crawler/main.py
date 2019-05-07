import requests
import os
from lxml import html
from urllib.parse import urljoin

class DeepCrawler:
    def __init__(self, start_page):
        self.visited_url = {}
        self.queue_url = [start_page]
        self.folder_name = 'LINKS/' + start_page.split('.')[1].upper()


    def get_url_list(self, url):
        print('crawling: %s'%(url))
        
        try:
            url = str.replace(url.lower(), '\n','')
            response = requests.get(url, timeout=10.0)
            raw_html = response.text
            parsed_html = html.fromstring(raw_html)
        except:
            return
        
        url_title_item = parsed_html.xpath('//title')
        url_title = '(NO TITLE)'
        try:
            url_title = url_title_item[0].text
        except:
            url_title = '(ERROR TITLE)'
        self.visited_url[url] = url_title
    
        for a in parsed_html.xpath('//a'):
            raw_url = a.get('href')
            if raw_url is None:
                continue
            
            parsed_url = urljoin(url, raw_url)
            if parsed_url not in list(self.visited_url.keys()) and parsed_url not in self.queue_url:
                self.queue_url.append(parsed_url)
    
    def output_result(self):
        urls = list(self.visited_url.keys())

        if not os.path.exists(self.folder_name):
            print('Create project' + self.folder_name)
            os.makedirs(self.folder_name)
        f = open(self.folder_name + '/data.txt', 'w+', encoding='utf-8')

        for url in urls:
            f.write(url + '\n')
        f.close()

        
    def start_crawling(self, threshold=-1):
        while threshold is not 0:
            this_url = self.queue_url[0]
            self.get_url_list(this_url)
            
            if len(self.queue_url) == 1:
                break
            else:
                self.queue_url = self.queue_url[1:]
                
            threshold -= 1
        
        self.output_result()
        print('DONE!')
        
        
PATHS = open('Links_Crawler\links.txt').readlines()
for PATH in PATHS:        
    myCrawler = DeepCrawler(PATH)
    myCrawler.start_crawling(threshold=10000)