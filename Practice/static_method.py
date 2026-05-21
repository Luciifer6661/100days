class Math:
    
    def __init__(self, num):
        self.num1=num
        
    def addition(self,n):
        self.num1=self.num1+n
        return self.num1
    
    @staticmethod
    def add(a,b):
        return a+b
m=Math(8)
print(m.addition(2))
print(a.num)
print(m.add(3,11))
print(Math.add(3,12))
