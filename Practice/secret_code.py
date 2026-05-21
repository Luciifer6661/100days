import random
import string

msg=input("Enter your message")
def secret_message_encode(msg1):
    lst=[]
    if len(msg)<3:
        for i in msg1:
            lst.append(i)
        # lst.reverse()
        lst=lst[::-1]
        new1="".join(lst)
        # print(new1)
        return new1
        
    else:
        for i in msg1:
            lst.append(i)
        l=lst.pop(0)
        lst.append(l)
        
        random_f3 = random.sample(string.ascii_lowercase, 3)
        random_l3 = random.sample(string.ascii_lowercase, 3)
        new=random_f3+lst+random_l3
        new1="".join(new)
        # print(new1)
        return new1

def secret_msg_decode(message):
    lst2=[]
    if len(encoded)<3:
        for i in encoded:
            lst2.append(i)
        lst2.reverse()
        new2="".join(lst2)
        return new2
    else:
        for i in encoded:
            lst2.append(i)
        lst2=lst2[3:len(lst2)-3:]
        popp=lst2.pop()
        lst2.insert(0,popp)
        new2="".join(lst2)     
        return new2
        
    
    

encoded=secret_message_encode(msg)
print(encoded)

decoded=secret_msg_decode(encoded)
print(decoded)