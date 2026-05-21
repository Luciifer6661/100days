def findMax(lst):
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
            
    return max

print(findMax([2,56,78,9,40,100,109,786]))

def findMin(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
            
    return min

print(findMin([2,56,78,9,40,100,109,786]))