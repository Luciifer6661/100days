'''Question:
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
'''

class American:
    
    @staticmethod
    def printNationality():
        print ("America")
        
obj=American()
obj.printNationality()
American.printNationality()


'''Question:
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.'''

class Americans():
    print("Americans class")
    
class NewYorker(Americans):
    print("New Yorker class")
        
obj2=Americans()
obj3=NewYorker()

'''Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.
'''

class circle:
    def __init__(self,r):
        self.radius=r
    
    def areaofcircle(self):
        area=3.14*self.radius**2
        print(area)
        
cir=circle(7)
cir.areaofcircle()

'''Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.'''

class rectangle:
    
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    
    def areaOfRect(self):
        return self.length*self.breadth
    
rect=rectangle(10,6)
print(rect.areaOfRect())


'''Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
'''

class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class square(shape):
    
    def __init__(self,l):
        super().__init__()
        self.length=l

    def area(self):
        return self.length**2

obj_shape=shape

obj_square=square(5)
print(obj_square.area())

        