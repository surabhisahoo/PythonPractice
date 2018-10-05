d = {}

with open('romeo') as o:
    l = o.readline()
    l = l.split(" ")
    for i in l:
        d[i] = i
print(d)

for k in d:
    if k == 'sofweedt':
        print("available")
    else:
        print("not availablke")
