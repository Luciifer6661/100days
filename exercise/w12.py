'''Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
lst=[]
for i in range(2000,3001):
    counter=0
    
    str1=str(i)
    for j in str1:
        s=int(j)
        if s%2==0:
            # print(j," ")
            counter+=1
    if counter==4:

        lst.append(str1)            

print(lst)     
        
