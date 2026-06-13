'''Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].'''

num=[1,2,3,4,5,6,7,8,9,10]

mapped=map(lambda x: x**2,num)
print(type(mapped))
print(list(mapped))

'''Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''

num2=[1,2,3,4,5,6,7,8,9,10]
newlist=list(filter(lambda x: x%2==0, num2 ))
newlist2=list(map(lambda x: x**2, newlist))

print(newlist2)

#or

num3=[1,2,3,4,5,6,7,8,9,10]
newlist3=list(map(lambda x: x**2 ,filter(lambda x: x%2==0, num2 )))

print(newlist3)

'''Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''


newlist4=list(filter(lambda x: x%2==0 ,range(1,21)))
print(newlist4)


'''Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).'''


newlist5=list(map(lambda x: x**2,range(1,21)))
print(newlist5)