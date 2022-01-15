""" Write a Python program to sum all the items in a dictionary."""
# Creating a dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using for loop to find sum of values
sum = 0
for i in d.values():
    sum = sum + i
print(sum)
