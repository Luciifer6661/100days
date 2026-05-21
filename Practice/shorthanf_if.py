#short hand if-else
a=9999
b=999
print(a) if a<b else print(b) if a>b else print("=")

c=9 if a>b else""
print(c)

#enumerate function
marks=[12,44,5,66,87,23]
for mark, index in enumerate(marks, start=1):
    print(mark, index) 
    
import math
print(dir(math))
