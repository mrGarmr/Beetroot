# Implement a stack using a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Head of the linked list is the top of the stack
        self.size = 0    # Track the number of elements

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push: Add an item to the top of the stack
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top  # New node points to current top
        self.top = new_node       # Update top to new node
        self.size += 1

    # Pop: Remove and return the top item from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        popped_item = self.top.data
        self.top = self.top.next  # Move top to the next node
        self.size -= 1
        return popped_item

    # Peek: Return the top item without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        return self.top.data

    # Get the size of the stack
    def get_size(self):
        return self.size

    # Display the stack (for testing)
    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

# Testing the implementation
if __name__ == "__main__":
    stack = Stack()
    
    # Test push
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("After push 1, 2, 3:", stack)  # [3, 2, 1]
    
    # Test peek
    print("Top item (peek):", stack.peek())  # 3
    
    # Test pop
    popped = stack.pop()
    print("Popped item:", popped)  # 3
    print("After pop:", stack)    # [2, 1]
    
    # Test size
    print("Stack size:", stack.get_size())  # 2
    
    # Test empty pop
    stack.pop()
    stack.pop()
    print("After popping all:", stack)  # []
    try:
        stack.pop()
    except IndexError as e:
        print(e)  # Cannot pop from an empty stack
    
    # Test empty peek
    try:
        stack.peek()
    except IndexError as e:
        print(e)  # Cannot peek an empty stack