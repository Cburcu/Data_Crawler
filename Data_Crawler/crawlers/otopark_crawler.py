def otopark_crawler(f, soup):
    html_tags = soup.find_all('div', {"class": "message-content js-messageContent"})
    if html_tags != []:
        for html_tag in html_tags:
            tags = html_tag.text
            if tags != None:
                model_file = f.readlines()
                if tags not in model_file:
                    f.write(tags.strip()+'\n')
                    print(tags)
                else:
                    print('model is in models file')
            else:
                print('empty tag\n')
                continue