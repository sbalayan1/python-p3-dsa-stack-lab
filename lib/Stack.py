class Stack:

    def __init__(self, items = [], limit = 100):
        pass
        self.limit = limit
        self.items = [items[idx] for idx in range(0, min(len(items), limit))]

    def isEmpty(self):
        pass
        return len(self.items) == 0

    def push(self, item):
        pass
        if not self.full(): self.items.insert(0, item)

    def pop(self):
        pass
        return self.items.pop(0)

    def peek(self):
        pass
        return self.items[-1]
    
    def size(self):
        pass
        return len(self.items)

    def full(self):
        pass
        return len(self.items) == self.limit

    def search(self, target):
        pass
        for idx, item in enumerate(self.items):
            if item is target: return 0 + idx

        return -1
