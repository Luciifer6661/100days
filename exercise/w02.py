def w02(x):
    
    if x==0 or x==1:
        return 1
    else:
       return x*w02(x-1)
x=int(input())
print(w02(x))