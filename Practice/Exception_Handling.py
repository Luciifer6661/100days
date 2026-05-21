num=int(input("Enter a number:"))
try:
    lst=[1,5,9,4]
    print(lst[num])
    

except IndexError:
    print("Index error out of range")

finally:
    print("End of programme")