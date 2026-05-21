class Employee:
    def __init__(self,name,id):
        self._name=name
        self._id=id
        
    def show(self):
        print(f"The name of employee is {self._name} with Employee ID {self._id}")


class child(Employee):
    
    def test(self):
        print("Hi Employee")
        
        
class sub_child(child):
    def new():
        pass
  
        
e1=Employee("Rohan",400)
e1.show()
e2=child("Karan",125)
e2.show()
e3=sub_child("Rohit",554)
e3.show()
e2.test()