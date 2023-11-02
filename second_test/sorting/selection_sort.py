"""
Lógica do selection sort: em cada iteração, o inésimo item de uma lista é comparado com cada elemento posterior até que
um valor menor seja encontrado. Ao encontrar, suas posições são trocadas.
"""


def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        for j in range(i+1, n):
            if theSeq[j] < theSeq[i]:
                theSeq[i], theSeq[j] = theSeq[j], theSeq[i]


teste = [5, 2, 3, 7, 5, 8, 9, 1]

selectionSort(teste)
print(teste)