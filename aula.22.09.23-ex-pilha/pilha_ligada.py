class Node:
    def __init__(self, info, next):
        self.info = info
        self.next = next


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        if not self.isEmpty():
            return self._top.info
    
    def pop(self):
        if not self.isEmpty():
            node = self._top
            self._top = self._top.next
            self._size -= 1
            return node.info
    
    def push(self, value):
        new = Node(value, self._top)
        self._top = new
        self._size += 1