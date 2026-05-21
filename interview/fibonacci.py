def fibonacci(n):
    if n==0:
        return print("number should be gt than 0")
    elif(n==1):
        return 1
    elif(n==2):
        return print(0,1)
    else:
        a=0
        b=1
        a,b=b,a+b
        
        
# fib = [0,1]
# # Range starts from 0 by default
# for i in range(5):  
#     fib.append(fib[-1] + fib[-2]) 
    

# # Converting the list of integers to string
# print(', '.join(str(e) for e in fib))