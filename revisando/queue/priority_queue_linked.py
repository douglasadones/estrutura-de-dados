## We could using a dictionary where each key it's the priority and all the values
## its a list with all the items with the same priority. Warning! Node only need the 'item' information.

class Node:
    def __init__(self, queue_number, item, next=None) -> None:
        self.queue_number = queue_number
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

    def enqueue(self, queue_number, item) -> None:
        new_node = Node(queue_number, item)
        if self.isEmpty():
            self.qtail = self.qhead = new_node
        else:
            # Here I need to sort all the pointers in order to keep the nodes' priority
            if new_node.queue_number < self.qhead.queue_number:  # max priority (qhead)
                new_node.next = self.qhead
                self.qhead = new_node
            elif new_node.queue_number >= self.qtail.queue_number: # min priority (qtail)
                self.qtail.next = new_node
                self.qtail = new_node
            else:  # finding the right place through the Queue.
                previous_node = self.qhead
                next_node = previous_node.next
                while next_node is not None:
                    if new_node.queue_number < next_node.queue_number:
                        previous_node.next = new_node
                        new_node.next = next_node
                        break
                    previous_node, next_node = next_node, next_node.next
        self.size += 1
        print(f'Size: {self.size}')

    def dequeue(self):
        deleted_node = self.qhead
        self.qhead = self.qhead.next
        return deleted_node

    def show(self):
        temp = self.qhead
        while temp is not None:
            print(f'{temp.item:<2} | Priority: {temp.queue_number}')
            temp = temp.next
