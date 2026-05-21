str1="Slient"
str2="Listen"

lst1=list(str1.upper())
lst2=list(str2.upper())
lst1.sort() == lst2.sort()
if lst1==lst2:
    print(lst1)
    print(lst2)
    print("True")
else:
    print("false")