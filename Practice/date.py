import time
timestamp=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
if (hour>0 and hour<12):
    print("Good Morning")
elif(16<hour<20):
    print("Good Evening")
else:
    print("Good Night")
# print(time.strftime("%A:%M:%S"))