class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        popped_item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        return self.top.data

    def get_size(self):
        return self.size

    # New method: get_from_stack
    def get_from_stack(self, e):
        if self.is_empty():
            raise ValueError(f"Element {e} not found in the stack: stack is empty")
        
        # Temporary stack to preserve order
        temp_stack = Stack()
        found = False
        result = None
        
        # Pop elements and search for e
        while not self.is_empty():
            current = self.pop()
            if current == e and not found:  # Take first occurrence
                found = True
                result = current
            else:
                temp_stack.push(current)
        
        # Restore elements back to original stack
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        
        if not found:
            raise ValueError(f"Element {e} not found in the stack")
        
        return result

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"


# _______________________________________
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        dequeued_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue")
        return self.front.data

    def get_size(self):
        return self.size

    # New method: get_from_stack (should be get_from_queue, but following task naming)
    def get_from_stack(self, e):
        if self.is_empty():
            raise ValueError(f"Element {e} not found in the queue: queue is empty")
        
        # Temporary queue to preserve order
        temp_queue = Queue()
        found = False
        result = None
        
        # Dequeue all elements and search for e
        while not self.is_empty():
            current = self.dequeue()
            if current == e and not found:  # Take first occurrence
                found = True
                result = current
            else:
                temp_queue.enqueue(current)
        
        # Restore elements back to original queue
        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())
        
        if not found:
            raise ValueError(f"Element {e} not found in the queue")
        
        return result

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

# Testing the Queue extension
if __name__ == "__main__":
    
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Original queue:", queue)  # [1, 2, 3]
    
    # Test get_from_stack (element exists)
    result = queue.get_from_stack(2)
    print("Found element:", result)  # 2
    print("Queue after get_from_stack(2):", queue)  # [1, 2, 3]
    
    # Test get_from_stack (element not found)
    try:
        queue.get_from_stack(4)
    except ValueError as e:
        print(e)  # Element 4 not found in the queue
    
    # Test on empty queue
    empty_queue = Queue()
    try:
        empty_queue.get_from_stack(1)
    except ValueError as e:
        print(e)  # Element 1 not found in the queue: queue is empty