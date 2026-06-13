'''Please raise a RuntimeError exception.

Hints:

Use raise() to raise an exception.
'''

# raise RuntimeError('something wrong')

'''Write a function to compute 5/0 and use try/except to catch the exceptions.'''
def exception1():
    try:
        a=5/0
    except ZeroDivisionError:
        print("Cannot divide by zero")
exception1()


'''Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.
'''
class AgeError(Exception):
    def __init__(self, msg):
        self.msg = msg

class NameError(Exception):
    def __init__(self, msg):
        self.msg = msg

def validate_person(name, age):
    if len(name) < 2:
        raise NameError("Name must be at least 2 characters")
    if age < 0 or age > 120:
        raise AgeError("Age must be between 0 and 120")
    return f"Valid: {name}, {age}"

try:
    print(validate_person("John", 12))
except NameError as e:
    print(f"Name Error: {e.msg}")
except AgeError as e:
    print(f"Age Error: {e.msg}")