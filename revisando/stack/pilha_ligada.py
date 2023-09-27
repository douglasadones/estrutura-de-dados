class Node:
    def __init__(self, info, link=None):
        self.info = info
        self.next = link


class Stack:
    def __init__(self):
        self._top = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def pop(self):
        if not self.isEmpty():
            temp = self._top
            self._top = temp.next
            self.size -= 1
            return temp.info
    
    def peek(self):
        if not self.isEmpty():
            return self._top.info
    
    def push(self, item):
        temp = Node(item, self._top)
        self._top = temp
        self.size += 1