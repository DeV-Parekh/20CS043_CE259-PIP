""" Write a Python program to remove an item from a set if it is present in the set. 
    STUDENT ID:-    20CS043
    STUDENT NAME:-  DEV PAREKH
"""
'''
    remove() or discard() can be used
'''

# remove()
s = {'a', 'b', 'c', 'd', 'e'}
s.remove('e')
print(s)
# s.remove('f') will give error as 'f' not present in s
'''
s.remove('f')
print(s)
'''

# discard()
s.discard('d')
print(s)
# s.discard('f') wont give error
s.discard('f')
print(s)
