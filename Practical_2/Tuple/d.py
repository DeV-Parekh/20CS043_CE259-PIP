"""Write a Python program to convert a tuple to a string."""
'''
    Method 1
    using join() method
'''
t = ('p', 'q', 'r')
string_t = ''.join(t)
print(type(string_t))
print(string_t)

'''
    Method 2
    Using for loop
'''
# Creating an empty string
string_t_new = ''

# Adding each item of tuple in string
for i in t:
    string_t_new = string_t_new + i
print(type(string_t_new))
print(string_t_new)
