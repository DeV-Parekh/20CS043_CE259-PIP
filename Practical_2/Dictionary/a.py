""" Write a Python script to check whether a given key already exists in a dictionary.
    STUDENT ID:-    20CS043
    STUDENT NAME:-  DEV PAREKH
"""
# Creating a dictionary
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
a = 2

# Checking if key a is present or not
if a in d:
    print("Given key:", a, " present")
else:
    print("Given key:", a, " NOT present")
