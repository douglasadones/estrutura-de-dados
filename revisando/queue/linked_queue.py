class Node:
    def __init__(self, item, next=None) -> None:
        self.item = item
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.qhead = None
        self.qtail = None
        self.count = 0

    def isEmpty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        return self.count

    def enqueue(self, item) -> None:
        new_node = Node(item)
        if self.isEmpty():
            self.qhead = new_node
            self.qtail = new_node
        else:
            self.qtail.next = new_node
            self.qtail = new_node
        self.count += 1

    def dequeue(self):
        if not self.isEmpty():
            removed_node = self.qhead
            self.qhead = self.qhead.next
            self.count -= 1
            return removed_node.item