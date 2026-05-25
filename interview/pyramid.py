#   *
#  * *
# * * *

# This one
    #   *
    #  ***
    # *****
    #*******
  # *********
# Min level : 3
# level can be a Even number


def pyramid1(floor):
    height=2*floor-1
    for i in range(1,height+1):
        
        print("*"*i)        
pyramid1(3)


def centered_py():
    n = 5
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * i
        print(spaces + stars)
centered_py()