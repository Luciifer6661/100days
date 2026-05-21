x=int(input("Enter a number: "))

match x:
    case 1:
        print("x is 1")
    case 6:
        print("x is 6")
    case _ if (x<6):
        print("x is less than ")
    case _ if (x%2==0):
        print ("x is greater than 6")
    case _:
        print("x is something else")