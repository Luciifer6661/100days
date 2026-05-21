def appl(fx,value):
    return value + fx(value)

half=lambda x : x/2
print(appl(half,66))

