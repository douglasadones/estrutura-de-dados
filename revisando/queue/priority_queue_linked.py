class Node:
    def __init__(self, priority, item, next=None) -> None:
        self.priority = priority
        self.item = item
        self.next = next


class LinkedPriorityQueue:
    def __init__(self) -> None:
        self.qhead = None
        self.qtail = None
        self.size = 0
    
    def isEmpty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def enqueue(self, priority, item) -> None:
        new_node = Node(priority, item)
        if self.isEmpty():
            self.qtail = self.qhead = new_node
        else:
            self.qtail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        highest_priority = self.qtail.priority
        temp = self.qhead
        while temp != self.tail:  # Loop to take the highest priority node
            if temp.priority > highest_priority:
                highest_priority = temp.priority
            temp = temp.next

        previous_node = self.qhead
        current_node = previous_node.next

        while current_node.priority != highest_priority:  # loop to remove the node.
            if current_node.priority == highest_priority:
                deleted_node = current_node
                previous_node.next = current_node.next
            previous_node = previous_node.next
        self.size -= 1
        return deleted_node
