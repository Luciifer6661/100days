'''Print a unicode string "hello world".

Hints:

Use u'strings' format to define unicode string.


All strings in python are unicode by default
'''

from traitlets import Unicode


unicodeString = u"नमस्ते"
print (unicodeString)


'''Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:
'''

s = input()
u = s.encode('utf-8')
print (u)
d=u.decode('utf-8')
print(d)

'''Write a special comment to indicate a Python source code file is in unicode.

Hints:

Solution:
'''
#-*- coding: utf-8 -*-