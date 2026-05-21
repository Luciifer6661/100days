x=10

def hello():
    global x
    x=5
    print(x)

hello()
print(x)