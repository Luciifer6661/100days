#Public

# class Employee:
#     def __init__(self):
#         self.name="Shikhar"
        
# e=Employee()
# print(e.name)


#Private

# class Employee:
#     def __init__(self):
#         self.__name="Shikhar"
        
# e=Employee()
# print(e._Employee__name)

# print(e.__dir__())


#Protected

class Student:
    def __init__(self):
        self._name = "Harry"
    def _funName(self):      # protected method
        return "CodeWithHarry"
class Subject(Student):       #inherited class
    pass
obj = Student()
obj1 = Subject()
# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())

