import os

def link_data(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                rel_dir = os.path.relpath(r, path)
                rel_file = path + '/' + rel_dir + '/' + file
                files.append(rel_file)
    return files