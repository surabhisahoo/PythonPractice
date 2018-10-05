file = input("Enter file name: ")

with open(file, 'r') as o:
    lines = o.readlines()
    for line in lines:
        r = line.find('DSPAM')
        if r > 0:
            a = line.split(':')
            print(a)
            print(a[-1].lstrip())
            with open('writetext.txt','a') as w:
                w.write(line.lstrip())


