'''Question:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float
'''

n=input("GIve a number:")

def compute(n):
    out=0
    lst=[]
    for i in range(1,n+1):
        out=out+float(i/(i+1))
        lst.append(out)
    return out
print(compute(5))


'''Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.
'''

def recur(n):
    if n>0:
        
        return recur(n-1)+100
    else:
        return 0
print(recur(5))