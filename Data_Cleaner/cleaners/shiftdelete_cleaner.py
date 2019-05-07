def shiftdelete_cleaner(text, file_write):
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
                    file_write.write(line + '\n')