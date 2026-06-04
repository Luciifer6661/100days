'''Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''

lst=[]
numbers="1,2,3,4,5,6,7,8,9"
integers=numbers.split(',')
for i in integers:
    inte=int(i)
    if inte%2!=0:
        lst.append(inte**2)
        
print(lst)

"OR"

# Read input
numbers = list(map(int, input("Enter comma-separated numbers: ").split(',')))

# Square each odd number using list comprehension
squared_odds = [num ** 2 for num in numbers if num % 2 != 0]

# Print result
print(squared_odds)