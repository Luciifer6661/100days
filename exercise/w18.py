'''A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''

import re
password="ABd1234@1,a F1#,2w3E*,2We3345, ACd54674#2"
lst_pass=password.split(",")

lst_auth=[]

for i in lst_pass:
    if 6<=len(i)<=12:
        caps=len(re.sub("[^A-Z]","",i))
        lower=len(re.sub("[^a-z]","",i))
        num=len(re.sub("[^0-9]","",i))
        special=len(re.sub("[\w]","",i))
        if caps and lower and num and special > 0:
            lst_auth.append(i)
        
        
    # else:
    #     print("no other password matched the criteria")
        
print(f" These passwords matched the criteria {lst_auth}")