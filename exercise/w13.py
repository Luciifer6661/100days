'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

import re
sentence="hello world! 123"
letter=0
number=0
for i in sentence:
    # print(i)
    if i in re.sub("[^A-Za-z]","",sentence):
        letter+=1
    elif i in re.sub("[0-9]","",sentence):
        number+=1   
print("letter=",letter)
print("number=",number)