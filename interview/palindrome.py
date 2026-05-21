str1="Kaghgak"
lst1=[]
for ch in str1.upper():
    lst1.append(ch)

lst2=lst1[::-1]
print(lst1)
print(lst2)


if lst2==lst1:
    print("palindrome")
else:
    print("false")
    

def count_space(msg):
    print (msg.count(" "))
    
count_space("This is a beautifula day")


    