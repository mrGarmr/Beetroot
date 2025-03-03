# Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty(): 
            return None  # Return None if stack is empty
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


def reverse_input(input_string):
    '''A program that reads in a sequence of characters and prints them in reverse order'''
    stack = Stack()
    
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

input_string = input("Enter a sequence of characters: ")
reversed_string = reverse_input(input_string)
print(f"Reversed sequence: {reversed_string}")
