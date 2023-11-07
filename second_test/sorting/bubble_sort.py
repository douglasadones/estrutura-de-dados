"""
Lógica do bubble sort: A cada iteração, o maior valor é posicionado no final da lista.
"""


def bubbleSort(theSeq):  # Levando o maior valor para o final
    n = len(theSeq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            first = theSeq[j]
            second = theSeq[j+1]
            if first > second:
                theSeq[j], theSeq[j+1] = theSeq[j+1], theSeq[j]
