d = {}

with open('romeo') as o:
    lines = o.readlines()
    for line in lines:
        l = line.split(" ")
        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
print(d)
# to display in readable format
for key in d:
    print(key,d[key])