# class person:
#     def __init__(self,age):
#         print("You are in the main class")
        
#         self._age=age
#         print("Age is ", self._age)
        
#     # @property  
# #getter
#     def get_age(self):
#         return self._age

# #setter
#     # @set_age.setter
#     def set_age(self,value):
#         self._age=value

# p=person(20)
# p.set_age(25)
# print(p.get_age())
# p=person(55)
# print(p.get_age())

#with property---------------------------------

# class person:
#     def __init__(self,age):
#         print("You are in the main class")
        
#         self._age=age
#         print("Age is ", self._age)
        
#     @property  
# #getter
#     def age(self):
#         return self._age

# #setter
#     @age.setter
#     def age(self,value):
#         self._age=value

# p=person(35)
# p.age=80
# print(p.age)


#Ex.2-------------------------------------------------------------

class MyClass:
    def __init__(self,value):
        self._value=value
        print(f"Value from __init__ {self._value}")

    def show(self):
        print(f"Value from show {self._value}")
    
    @property
    def ten_value(self):
        return 10* self._value
        # print(10*self.value)
    
    @ten_value.setter
    def ten_value(self,new):
        self._value=new
        
obj=MyClass(10)
obj.ten_value=20
print(obj.ten_value)
obj.show()
