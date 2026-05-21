import re
def count_digits_letters():
    name = 'Python is 133435235 klsdkfihj #$%@^& fghfg **'

    digitCount=re.sub("[^0-9]","",name)
    letterCount=re.sub("[^A-Za-z]","",name)
    spaceCount=re.findall("[ \n]",name)
    specialchar=re.sub("[\w]","",name)
    print(digitCount)
    print(letterCount)
    print(spaceCount)
    print(specialchar)
    
count_digits_letters()