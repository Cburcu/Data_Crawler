def shiftdelete_crawler(f, soup):
    html_tags = soup.find_all('div', {"class": "bbWrapper"})
    if html_tags != []:
        for html_tag in html_tags:
            tag = html_tag.text
            if tag != None:
                model_file = f.readlines()
                if tag not in model_file:
                    f.write(tag.strip()+'\n')
                    print(tag)
                else:
                    print('model is in models file')
            else:
                print('empty tag\n')
                continue