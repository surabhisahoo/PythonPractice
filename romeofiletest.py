l1 = []
with open ('romeo') as o:
   lines = o.readlines()
   print(lines)
   for line in lines:
       l = line.split(" ")
       for i in l:
           if i not in l1:
               l1.append(i)
print(l1)



