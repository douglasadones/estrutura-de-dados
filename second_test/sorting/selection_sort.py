"""
Lógica do selection sort: em cada iteração, o inésimo item de uma lista é comparado com cada elemento posterior até que
um valor menor seja encontrado. Ao encontrar, suas posições são trocadas.
"""


def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        smallest_pos = i
        for j in range(i+1, n):
            if theSeq[j] < theSeq[i]:
                smallest_pos = j
        if smallest_pos != i:
            theSeq[i], theSeq[smallest_pos] = theSeq[smallest_pos], theSeq[i]


teste = [5, 2, 3, 7, 5, 8, 9, 1]

selectionSort(teste)
print(teste)
