
path = 'Arabalar_Data\data.txt'
file = open(path, mode='r', encoding='utf8')
fileWrite = open('Arabalar_Data\Data.txt', mode='w', encoding='utf8')
text = file.readlines()
for line in text:

    if 'http' in line:
        continue
    else:
        sentences = line.split('.')
        for sentence in sentences:
            line = sentence.strip()
            if line is '':
                continue
            elif len(line) < 10:
                continue
            else:
                print(line)
                fileWrite.write(line + '\n')

file.close()
fileWrite.close()