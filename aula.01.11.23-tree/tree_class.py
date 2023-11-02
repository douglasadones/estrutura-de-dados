from queue_to_teste import Queue

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    


# percursoS em Profundidade.

def preorder(bintree):  # RED
    if bintree is not None:
        print(bintree.data)
        preorder(bintree.left)
        preorder(bintree.right)


def inorder(bintree):  # ERD
    if bintree is not None:
        inorder(bintree.left)
        print(bintree.data)
        inorder(bintree.right)


def posorder(bintree):  # EDR
    if bintree is not None:
        posorder(bintree.left)
        posorder(bintree.right)
        print(bintree.data)


# Percurso em largura: os nós são visitados por nível, da esquerda para a direita.

def breadthFirst(bintree):
    q = Queue()
    q.enqueue(bintree)
    while not q.isEmpty():
        node = q.dequeue()
        print(node.data)
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)
