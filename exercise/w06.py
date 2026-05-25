import math
def w06(n):
    d=n.split(",")
    lst=[]
    c=50
    h=30
    for i in d:
        w=math.sqrt((2*c*int(i))/h)
        lst.append(int(w))
        print()
    return lst

print (','.join((str(e) for e in w06('100,150,180'))))
