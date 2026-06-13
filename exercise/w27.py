'''With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line'''

tup=(1,2,3,4,5,6,7,8,9,10)

for i in range(0,int(len(tup))//2):
    print(i,"\w")
for i in range(int(len(tup))//2,int(len(tup))+1):
    print(i)