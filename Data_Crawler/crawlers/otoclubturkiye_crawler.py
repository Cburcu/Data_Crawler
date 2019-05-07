def otoclubturkiye_crawler(f, soup):
    html_tags = soup.find_all('div', {"class": "ipsColumn ipsColumn_fluid"})
    if html_tags != []:
        for html_tag in html_tags:
            tags = html_tag.find_all('p')
            for tag in tags:
                data_span = tag.text
                if data_span != None:
                    model_file = f.readlines()
                    if data_span not in model_file:
                        f.write(data_span.strip()+'\n')
                        print(data_span)
                    else:
                        print('model is in models file')
                else:
                    print('empty tag\n')
                    continue