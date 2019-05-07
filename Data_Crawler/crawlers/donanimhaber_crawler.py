def donanimhaber_crawler(f, soup):
    html_tags1 = soup.find_all('div', {"class": "forumkonusuicerigi"})
    if html_tags1 != []:
        for html_tag in html_tags1:
            tags = html_tag.find_all('span')
            for tag in tags:
                data_span = tag.text
                if data_span != None:
                    f.write(data_span.strip()+'\n')
                    print(data_span)
                else:
                    print('empty tag\n')
                    continue
    
    html_tags2 = soup.find_all('div', {"class": "icerik"})
    if html_tags2 != []:
        for html_tag in html_tags2:
            tags = html_tag.find_all('span')
            for tag in tags:
                data_span = tag.text
                if data_span != None:
                    f.write(data_span.strip()+'\n')
                    print(data_span)
                else:
                    print('empty tag\n')
                    continue

    html_tags3 = soup.find_all('div', {"class": "kl-tablo forum-page-kutu"})
    if html_tags3 != []:
        for html_tag in html_tags3:
            tags = html_tag.find_all('h3')
            for tag in tags:
                data_span = tag.text
                if data_span != None:
                    f.write(data_span.strip()+'\n')
                    print(data_span)                    
                else:
                    print('empty tag\n')
                    continue
    
    html_tags4 = soup.find_all('div', {"class": "yorum"})
    if html_tags4 != []:
        for html_tag in html_tags4:
            tags = html_tag.find_all('td')
            for tag in tags:
                data_span = tag.text
                if data_span != None:
                    f.write(data_span+'\n')
                    print(data_span)
                else:
                    print('empty tag\n')
                    continue