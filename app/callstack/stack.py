class Stack:
    def __init__(self):
        self.items = [{}]

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        return len(self.items)

    def __setitem__(self, key, value):
        # Implement custom logic to set values using bracket notation
        if not self.is_empty():
            self.peek()[key] = value

    def __getitem__(self, key):
        return self.peek()[key]
