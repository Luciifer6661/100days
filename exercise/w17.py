'''Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

'''
print("Enter amount with suffix D or W for Deposit and withdraw respectively")
amount=0
lst1=[]
while True:
    str1=input()
    if str1.upper()=="END":
        break
    lst1.append(str1)
for i in lst1:
    term=i[0]
    # print(int(i[2:len(i)+1]))
    if term.upper()=="D":
        amount=amount+int(i[2:len(i)+1])
    elif term.upper()=="W":
        amount=amount-int(i[2:len(i)+1])
    else:
        print("invalid input")
print(f"Total amount in your account is updated, Updated amount = {amount}")
        
        
