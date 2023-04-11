class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return 'ERROR: The stack is empty!'

    def is_empty(self):
        return self.items == [] 

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return 'ERROR: The stack is empty!'
    
    def size(self):
        return len(self.items)
        
    def clear(self):
        self.items = []

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items != []:
            return self.items.pop()
        raise IndexError('ERROR: The queue is empty!')
    
    def peek(self):
        if self.items != []:
            return self.items[len(self.items)-1]
        raise IndexError('ERROR: The queue is empty!')
        
    def clear(self):
        self.items = []
    
        
  