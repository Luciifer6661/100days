a=2
b=9
c=8
d=6

# def addu(a,b):
#     print(a+b)
    
# addu(a,b)
# addu(c,d)
# print(complex(a,b))

def average(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("Average is", sum/len(args))
average(1,2,3,4,5)

def fullname(**names):
    print("Hello, How are you Mr.",names["fname"])
    
fullname(fname="Shikhar",mname="Varshney",lname="Kaka")
    
        