def greetings(fx):
    def mfx(*args, **kwargs):
        
        print("Hello, How are You")
        fx(*args,**kwargs)
        print("Thanks You")
    return mfx
    
# @greetings
# def hello():
#     print("Hello World!")
    
# hello()

#OR

# greetings(hello)

@greetings
def add(a,b):
    print(a+b)

add(1,2)