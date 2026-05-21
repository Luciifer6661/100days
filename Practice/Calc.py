a=int(input("Enter a number:"))
b=int(input("Enter second number:",))
print("For Addition : 1\nMultiplication : 2\nDivision : 3\nSubtraction : 4")
c=int(input("Enter choice:",))
if c==1:
    print("Addition is:",a+b)
elif c==2:
    print("Multiplication is:",a*b)
elif c==3:
    print("Division is:",a/b)
elif c==4:
    print("Subtraction is:",a-b)
else:
    print("Invalid Choice")
    