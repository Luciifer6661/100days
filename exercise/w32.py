'''Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

'''



str1=["johny@gmail.com","sk@gmail.com"]
str3=[]
for i in str1:
    str2=i.split("@")
    print(str2)

    str3.append(str2[0])
print(str3)

import re

emailAddress = ["johny@gmail.com", "sk@gmail.com"]
pat2 = r"(\w+)@(\w+\.)+com"

for email in emailAddress:
    r2 = re.match(pat2, email)
    if r2:
        print(r2.group(1))

'''Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.'''

emailAddress = ["johny@gmail.com", "sk@google.com"]
pat2 = r"(\w+)@(\w+)\.+(com)"

for email in emailAddress:
    r2 = re.match(pat2, email)
    if r2:
        print(r2.group(2))
