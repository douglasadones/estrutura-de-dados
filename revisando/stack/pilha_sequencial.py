class Stack:
    def __init__(self):
        self._itens = list()

    def isEmpty(self):
        return len(self._itens) == 0

    def __len__(self):
        return len(self._itens)
    
    def peek(self):
        if not self.isEmpty():
            return self._itens[-1]
    
    def pop(self):
        if not self.isEmpty():
            return self._itens.pop()

    def push(self, item):
        self._itens.append(item)