l = [1,2,3,45,6,4]
def chop():
    l.pop(0)
    l.pop(-1)
    middle()

def middle():
    print(l)

chop()