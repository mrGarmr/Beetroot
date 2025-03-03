# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. 
# Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - 
# raise ValueError with proper info Message
 

# Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue. 
# Any other element must remain in the queue respecting their order. Consider the case in which the element is not found - 
# raise ValueError with proper info Message


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def get_from_stack(self, e):
        temp_stack = []
        found = False
        result = None
        
        while self.stack:
            item = self.stack.pop()
            if item == e:
                result = item
                found = True
                break
            else:
                temp_stack.append(item)
        # [1, 2, 3, 4, 5], [1,2,], [4, 5]


        while temp_stack:
            # print('TEMP',temp_stack)
            # print('STACk', self.stack)
            self.stack.append(temp_stack.pop())
        
        if not found:
            raise ValueError(f"Element {e} not found in stack")
        
        return result

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
assert(stack.stack == [1, 2, 3, 4, 5])
print('I found: ', stack.get_from_stack(3))  
assert(stack.stack == [1, 2, 4, 5])
print('Stack after picking e', stack.stack)  

print(100*'_')


class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from empty queue")
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Peek from empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def get_from_queue(self, e):
        temp_queue = []
        found = False
        result = None
        
        while self.queue:
            item = self.queue.pop()
            if item == e:
                result = item
                found = True
                break
            else:
                temp_queue.append(item)
        
        while temp_queue:
            self.queue.append(temp_queue.pop())
        
        if not found:
            raise ValueError(f"Element {e} not found in queue")
        
        return result


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
assert(queue.queue == [1, 2, 3, 4, 5])
print('I found: ', queue.get_from_queue(3))  
print('Queue after picking e', queue.queue)  # Output: [1, 2, 4]
assert(queue.queue == [1, 2, 4, 5])

