""" Write a Python script to merge two Python dictionaries. 
    STUDENT ID:-    20CS043
    STUDENT NAME:-  DEV PAREKH
"""
# Creating 2 dictionaries
d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
d2 = {5: 'e', 6: 'f', 7: 'g', 8: 'h'}

# Merging 2 dictionaries with **
d3 = {**d1, **d2}
print(d3)
