#Count who won?
votes = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]
d = {}
for i in votes:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d)


########### Find Factorial of a number #######################
fact = 1
for i in range(1, 6):
    fact = fact * i
print(fact)

############# Fibonacci Series ######################

a = 0
b = 1
for i in range(10):
    print(a)
    a,b = b,a+b

######################################
