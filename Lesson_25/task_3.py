# Implement a queue using a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Head of the list (where we dequeue)
        self.rear = None   # Tail of the list (where we enqueue)
        self.size = 0      # Track the number of elements

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Enqueue: Add an item to the rear of the queue
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node  # Link the new node at the rear
            self.rear = new_node       # Update rear to the new node
        self.size += 1

    # Dequeue: Remove and return the front item from the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        dequeued_item = self.front.data
        self.front = self.front.next  # Move front to the next node
        if self.front is None:        # If queue is now empty, reset rear
            self.rear = None
        self.size -= 1
        return dequeued_item

    # Peek: Return the front item without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue")
        return self.front.data

    # Get the size of the queue
    def get_size(self):
        return self.size

    # Display the queue (for testing)
    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

# Testing the implementation
if __name__ == "__main__":
    queue = Queue()
    
    # Test enqueue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("After enqueue 1, 2, 3:", queue)  # [1, 2, 3]
    
    # Test peek
    print("Front item (peek):", queue.peek())  # 1
    
    # Test dequeue
    dequeued = queue.dequeue()
    print("Dequeued item:", dequeued)  # 1
    print("After dequeue:", queue)     # [2, 3]
    
    # Test size
    print("Queue size:", queue.get_size())  # 2
    
    # Test empty dequeue
    queue.dequeue()
    queue.dequeue()
    print("After dequeuing all:", queue)  # []
    try:
        queue.dequeue()
    except IndexError as e:
        print(e)  # Cannot dequeue from an empty queue
    
    # Test empty peek
    try:
        queue.peek()
    except IndexError as e:
        print(e)  # Cannot peek an empty queue
