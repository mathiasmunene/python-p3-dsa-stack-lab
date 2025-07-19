class Stack:
    def __init__(self, items=None, limit=None):
        self.items = [] if items is None else list(items)
        self.limit = limit
    
    def push(self, value):
        if self.full() and self.items:
            self.items[-1] = value  # Overwrite top item when full
        else:
            self.items.append(value)
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def full(self):
        return self.limit is not None and len(self.items) >= self.limit
    
    def search(self, value):
        try:
            return self.items[::-1].index(value)
        except ValueError:
            return -1