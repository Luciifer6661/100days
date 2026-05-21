from random import shuffle
def randomize_list(lst):
    shuffle(lst)
    return lst

lst=['Shikhar','29','Pune', 'Holiday']
print(randomize_list(lst))