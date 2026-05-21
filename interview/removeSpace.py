import re
str1="This is a beautiful day and good Morning C O D E"
lst=[]
for ch in str1:
    if ch in re.sub("[^a-zA-Z]","",str1):
        lst.append(ch)
    elif ch==re.findall("[ \n]",str1):
        pass
string1=''.join(str(e) for e in lst)
print(string1)


#or

import re

string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)
