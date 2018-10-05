l = [32,12,45,23,56,34]
large = l[0]
for i in l:
    if i > large:
        large = i
print(large)

#smallest number

small = l[0]
for x in l:
    if x < small:
        small = x
print(small)