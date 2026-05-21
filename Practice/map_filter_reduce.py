#MAP

# def cube(x):
#     return x*x*x

# l=[1,2,3,4,5]
# lst=[]
# for item in l:
#     lst.append(cube(item))
# print(lst)

#OR

# lst=list(map(cube,l))
# print(lst)

#OR

# lst=list(map(lambda x: x*x*x,l))
# print(lst)


#FILTER
# l=[1,2,3,4,5]
# def filter_func(a):
#     return a>3

# lst=list(filter(filter_func,l))
# print(lst)


#reduce
from functools import reduce

l=[1,2,3,4,5]
lst=reduce(lambda x,y:x+y, l)
print(lst)