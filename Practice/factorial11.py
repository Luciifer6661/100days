def factorial1 (n):
    if n>0:
        return n*factorial1(n-1)
    elif n==0 or n==1:
        return 1
print(factorial1(3))