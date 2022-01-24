# Function to create unique items list
def unique(lst):
    uniq = list()
    return [x for x in lst if not (x in uniq or uniq.append(x))]


# Taking length input
n = int(input())

# taking words input in list
lst = []
for i in range(n):
    lst.append(input())

# Creating a list having unique items
new_lst = unique(lst)

# Creating a list having count of items
output = []
for i in new_lst:
    output.append(lst.count(i))

# Printing length and items of list
print(len(output))
print(*output)
