class _Node:
    def __init__(self, priority, item) -> None:
        self.item = item
        self.priority = priority


class SequentialPriorityQueue:
    def __init__(self) -> None:
        self._itens = list()

    def isEmpty(self) -> bool:
        return len(self._itens) == 0
    
    def __len__(self) -> int:
        return len(self._itens)

    def enqueue(self, priority, item) -> None:
        new_node = _Node(priority, item)
        self._itens.append(new_node)

    def dequeue(self):
        if not self.isEmpty():
            highest_priority = self._itens[0]
            for i, item in enumerate(self._itens):
                if item.priority > highest_priority.priority:
                    highest_priority = item
            self._itens.remove(highest_priority)
            return highest_priority 
