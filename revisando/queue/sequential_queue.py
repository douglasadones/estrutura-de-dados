# TAD Queue - FIFO (First-In First-Out)
# Works just like a real world queue

class Queue:
    def __init__(self) -> None:
        self.itens = list()
    
    def isEmpty(self) -> bool:
        return len(self.itens) == 0

    def __len__(self) -> int:
        return len(self.itens)

    def enqueue(self, item) -> None:
        """Add the given item to the end of the queue"""
        self.itens.append(item)
    
    def dequeue(self):
        """Remove and return the first item of the queue."""
        if not self.isEmpty():
            return self.itens.pop(0)
    