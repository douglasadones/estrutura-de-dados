class QueueNode():
    def __init__(self, item) -> None:
        self.item = item
        self.next = 0


class Queue:
    def __init__(self) -> None:
        self.qhead = None
        self.qtail = None
        self.count = 0

    def isEmpty(self) -> bool:
        return self.count == 0
    
    def __len__(self):
        return self.count
    
    def enqueue(self, item) -> None:
        newNode = QueueNode(item)
        if self.isEmpty:
            self.qhead = newNode
        else:
            self.qtail.next = newNode
        self.qtail = newNode
        self.count += 1

    def dequeue(self):
        if not self.isEmpty:
            Node = self.qhead
            if self.qhead is self.qtail:
                self.qtail = None
            self.qhead = self.qhead.next
            self.count -= 1
            return Node
    
    
