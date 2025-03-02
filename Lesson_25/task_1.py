# Extend UnsortedList

# Implement append, index, pop, insert methods for UnsortedList. 
# Also implement a slice method, which will take two parameters 'start' and 'stop', 
# and return a copy of the list starting at the position and going up to but not including the stop position.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnsortedList:
    def __init__(self):
        self.head = None
        self.length = 0  # Track size for convenience

    def is_empty(self):
        return self.head is None

    # Append: Add an item to the end of the list
    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    # Index: Find the position of the first occurrence of an item
    def index(self, item):
        current = self.head
        position = 0
        while current:
            if current.data == item:
                return position
            current = current.next
            position += 1
        raise ValueError(f"{item} is not in the list")

    # Pop: Remove and return the item at the given position
    def pop(self, position=0):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty list")
        if position < 0 or position >= self.length:
            raise IndexError("Index out of range")
        
        if position == 0:
            popped_item = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            popped_item = current.next.data
            current.next = current.next.next
        self.length -= 1
        return popped_item

    # Insert: Add an item at the specified position
    def insert(self, position, item):
        if position < 0 or position > self.length:
            raise IndexError("Index out of range")
        
        new_node = Node(item)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1

    # Slice: Return a new UnsortedList from start to stop (exclusive)
    def slice(self, start, stop):
        if start < 0 or stop > self.length or start > stop:
            raise IndexError("Invalid slice range")
        
        result = UnsortedList()
        current = self.head
        position = 0
        
        # Move to start position
        while position < start and current:
            current = current.next
            position += 1
        
        # Copy elements from start to stop
        while position < stop and current:
            result.append(current.data)
            current = current.next
            position += 1
        
        return result

    # Helper method to display the list (for testing)
    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

# Testing the implementation
if __name__ == "__main__":
    ul = UnsortedList()
    
    # Test append
    ul.append(1)
    ul.append(2)
    ul.append(3)
    ul.append(4)
    print("After append:", ul)  # [1, 2, 3, 4]
    
    # Test index
    print("Index of 2:", ul.index(2))  # 1
    try:
        ul.index(5)
    except ValueError as e:
        print(e)  # 5 is not in the list
    
    # Test pop
    popped = ul.pop(1)
    print("Popped item:", popped)  # 2
    print("After pop:", ul)  # [1, 3, 4]
    
    # Test insert
    ul.insert(1, 5)
    print("After insert 5 at 1:", ul)  # [1, 5, 3, 4]
    
    # Test slice
    sliced = ul.slice(1, 3)
    print("Slice from 1 to 3:", sliced)  # [5, 3]