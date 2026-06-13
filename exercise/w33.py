'''Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use re.findall() to find all substring using regex.'''

import re
str1="2 cats and 3 dogs"
matchcase=re.findall("[0-9]",str1)
print(matchcase)
result = re.findall(r'\b\d+\b', str1) #b stands for boundary
print(result) 
result = re.findall(r'\d+', str1)
print(result) 
result = [w for w in str1 if w.isdigit()]
print(result)
print (re.findall("\d+",str1))
