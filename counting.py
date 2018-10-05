s = "surabhi sahoo"
d = {}
d1 = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)


for c in s:
    d1[c] = d1.get(c,0) + 1
print(d1)