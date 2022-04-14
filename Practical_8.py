# Implementing a Stack Data Structure
# using Class and Objects, with push, pop, and traversal method.
# (list implementation)
class Stack:

    # Initializing stack.
    def __init__(self):
        self.stack = []

    # Function to check if the stack is empty or not
    def is_Empty(self):
        return self.stack == []

    # Function to push the element using append()
    def push(self, value):
        self.stack.append(value)

    # Function to delete the top most element using pop()
    def pop(self):
        if self.is_Empty():
            print("Stack is Empty..\n")
        else:
            self.stack.pop()

    # Function to traverse the stack
    def traversal(self):
        print(f'Stack =  {self.stack[::-1]}')


# Creating object of class Stack
stack = Stack()

# Menu driven program for stack implementation
print("Enter the operation : \n")
while True:
    print("1. Push")
    print("2. Pop")
    print("3. IsEmpty")
    print("4. Traversal")
    print("5. Exit")

    operation = int(input())

    if operation == 1:
        print("Enter element to push in stack: ")
        stack.push(int(input()))

    elif operation == 2:
        stack.pop()

    elif operation == 3:
        print(f'Empty Status :', stack.is_Empty())

    elif operation == 4:
        stack.traversal()

    elif operation == 5:
        break

    else:
        print("Invalid choice!\n")
        continue
