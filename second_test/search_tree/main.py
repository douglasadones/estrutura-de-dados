from revisando.queue.linked_queue import Queue

# Classe do nó da árvore
class _Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Classe da árvore
class BinsearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def _minimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return None
        else:
            return self._minimum(subtree.left)

    def _maximum(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return None
        else:
            return self._maximum(subtree.right)

    def _height(self, subtree):
        if subtree is None:
            return -1
        else:
            hleft = self._height(subtree.left)
            hright = self._height(subtree.right)
            if hleft > hright:
                return hleft + 1
            else:
                return hright + 1

    def preorder(self, subtree):
        if subtree is not None:
            print(subtree, end=' ')
            self.preorder(subtree.left)
            self.preorder(subtree.right)

    def inorder(self, subtree):
        if subtree is not None:
            self.inorder(subtree.left)
            print(subtree, end=' ')
            self.inorder(subtree.right)

    def postorder(self, subtree):
        if subtree is not None:
            self.postorder(subtree.left)
            self.postorder(subtree.right)
            print(subtree, end=' ')

    def breadthFirst(self, subtree):
        q = Queue()
        if subtree is not None:
            q.enqueue(subtree)
            while not q.isEmpty():
                node = q.dequeue()
                print(node.data, end=' ')
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)

    def _search(self, subtree, value):
        if subtree is None:
            return None
        elif value < subtree.data:
            subtree.left = self.search(subtree.left, value)  #cuidado para não confundir o "subtree.left ="
        elif value > subtree.data:
            subtree.right = self.search(subtree.right, value)
        else:
            return subtree

    def _insert(self, subtree, value):
        if subtree is None:
            subtree = _Node(value)
        elif value < subtree.data:
            subtree.left = self.insert(subtree.left, value)
        elif value > subtree.data:
            subtree.right = self.insert(subtree.right, value)
        else:
            return subtree
    
    # O método insert é só um auxiliar desse método.
    def add(self, value):
        node = self._search(self._root, value)
        if node is None:
            self._root = self._insert(self._root, value)
            self._size += 1
            return True
        else:
            return False
    
    def _remove(self, subtree, target):
        pass
        