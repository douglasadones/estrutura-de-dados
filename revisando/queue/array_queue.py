from array import Array
# Queue ADT using a circular array

class Queue:
    def __init__(self, maxSize) -> None:
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array(maxSize)
    
    def isEmpty(self) -> bool:
        return self._count == 0
    
    def isFull(self) -> bool:
        return self._count == len(self._qArray)
    
    def __len__(self) -> int:
        return self._count
    
    def enqueue(self, item) -> None:
        if not self.isFull:
            maxSize = len(self._qArray)
            self._back = (self._back + 1) % maxSize  # calculo necessário já que o final é 'móvel'
            self._qArray[self._back] = item
            self._count += 1
    
    def dequeue(self):
        if not self.isEmpty():
            item = self._qArray[self._front]
            maxSize = len(self._qArray)
            self._front = (self._front + 1) % maxSize  # Classe array já deve ter ponteiros
            self._count -= 1
            return item
