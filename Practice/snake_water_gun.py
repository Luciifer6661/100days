import random

user1=int(input("What you want?\n 1. Snake\n 2. Water\n 3. Gun"))
user2=random.randint(1,3)
print(user2)
if user1==1 and user2==1:
    print("Tie")
elif user1==1 and user2==2:
    print("User1 Win!!")
elif user1==1 and user2==3:
    print("User2 Win!!")
elif user1==2 and user2==1:
    print("User2 Win!!")
elif user1==2 and user2==2:
    print("Tie")
elif user1==2 and user2==3:
    print("User1 Win!!")
elif user1==3 and user2==1:
    print("User1 Win!!")
elif user1==3 and user2==2:
    print("User2 Win!!")
else :
    print("Tie")
    
