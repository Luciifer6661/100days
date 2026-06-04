'''Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.'''

class dividebyseven:
    
    def __init__(self,n):
        self.n=n
    def generator(self):
        lst=[]
        i=0
        while i<self.n:
            if i%7==0:
                yield i
                i+=1
                

        
n=int(input("Enter a range:"))
obj=dividebyseven(n)

for num in obj.generator():
    print(num)