def filecuting(filename):
    f = open(filename, 'a+')
    f.write('========')
    f.seek(0, 0)
    atalks = []
    btalks = []
    count = 1

    for line in f:
        if line[:3] != '===':
            subject, talk = line.split(sep=':', maxsplit=1)
            if subject == 'A':
                atalks.append(subject + talk)
            elif subject == 'B':
                btalks.append(subject + talk)
        else:
            fa = open(f'a{str(count)}.txt', 'w')
            fb = open(f'b{str(count)}.txt', 'w')
            fa.writelines(atalks)
            fb.writelines(btalks)
            fa.close()
            fb.close()
            atalks.clear()
            btalks.clear()
            count += 1
    f.close()


filecuting('file.txt')
