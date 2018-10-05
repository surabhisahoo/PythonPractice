with open ('text1','r') as o:
    lines = o.readlines()
    print(lines)
    for line in lines:
        line = line.upper()
        with open('writetext.txt', 'w') as w:
            w.write(line)
