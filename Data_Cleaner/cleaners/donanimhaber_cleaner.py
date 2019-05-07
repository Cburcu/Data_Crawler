def donanimhaber_cleaner(text, file_write):
    for line in text:
        if '<' in line:
            continue
        elif 'http' in line:
            continue
        elif 'Http' in line:
            continue
        elif 'quote' in line:
            continue
        elif 'Alıntıları Göster' in line:
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
                    file_write.write(line + '\n')