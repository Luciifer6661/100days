name1=str(input("Enter your name:"))
amount=0
print("Hello,",name1,"Welcome to the game show Crorepati!")
start=str(input("Enter any key to start the game:"))
print("Here is your first question:")
print("Q1.Which of the following is not a programming language?")
print("1. HTML\n2. CSS\n3. Python\n4. Photoshop")
ans1=int(input("Enter your option(1-4):"))
if ans1==1:
    print("Sorry! Wrong Answer. You are eliminated.")
elif ans1==2:
    print("Sorry! Wrong Answer. You are eliminated.")
elif ans1==3: 
    print("Sorry! Wrong Answer. You are eliminated.")
elif ans1==4:
    print("Congratulations! Correct Answer.")
    amount=amount+1000
print("You have won Rs.",amount)
#second question

if amount>0:
    print("Here is your second question:")
    print("Q2.Which of the following is a snake?")
    print("1. Anaconda\n2. Python\n3. Cobra\n4. All of the above")
    ans2=int(input("Enter your option(1-4):"))
    if ans2==1:
        print("Sorry! Wrong Answer. You are eliminated.")
    elif ans2==3:
        print("Sorry! Wrong Answer. You are eliminated.")
    elif ans2==2: 
        print("Sorry! Wrong Answer. You are eliminated.")
    elif ans2==4:
        print("Congratulations! Correct Answer.")
        amount=amount*2
    print("You have won Rs.",amount)
    
if amount>0:
    print("Here is your third question:")
    print("Q3.Who is the CEO of Tesla?")
    print("1. Jeff Bezos\n2. Elon Musk\n3. Bill Gates\n4. Sundar Pichai")
    ans3=int(input("Enter your option(1-4):"))
    if ans3==1:
        print("Sorry! Wrong Answer. You are eliminated.")
    elif ans3==3:
        print("Sorry! Wrong Answer. You are eliminated.")
    elif ans3==4: 
        print("Sorry! Wrong Answer. You are eliminated.")
    elif ans3==2:
        print("Congratulations! Correct Answer.")
        amount=amount*2
    print("You have won Rs.",amount)
    
    
    

    