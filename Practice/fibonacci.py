# def fibonacci(n):
#     if n <= 0:
#         return "Input should be a positive integer."
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n+1):
#             a, b = b, a + b
#         return b
    
# print(fibonacci(0))

def ffibonacci(n):
    if n==0:
        return 0
    else:
        a=0
        b=1
        for i in range(n+1):
            print(a, end=",")
            a,b=b,a+b   
          
ffibonacci(5)
