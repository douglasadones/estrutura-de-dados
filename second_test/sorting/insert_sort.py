"""
A lógica aqui é armazenar o valor que vc quer reposicionar, realocar os outros elementos para a direita
e então adicionar o valor salvo na posição livre.
"""

def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value



teste = [5, 3, 8, 66, 9, 15, 2, 1, 7, 4]

insertionSort(teste)

print(teste)
