""" Write a Python program to add an item in a tuple 
    STUDENT ID:-    20CS043
    STUDENT NAME:-  DEV PAREKH
"""
# Creating a tuple
t = ('DeV', 43, 9.89, True)

''' 
    Method 1
    Merging two tuples with +
'''
new_t = t + ('new_item',)
print(new_t)

''' 
    Method 2
    Converting tuple into list and appending and finally converting into tuple
'''

# converting into list
list_t = list(t)

# appending item
list_t.append('new_item_list')

# converting into tuple again
converted_tupple = tuple(list_t)
print(converted_tupple)
