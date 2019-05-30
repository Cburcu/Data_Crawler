
def read_brand_list(path):
    file = open(path, 'r', encoding='utf-8')
    lines = file.readlines()

    return lines