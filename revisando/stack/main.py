# from pilha_seq import Stack
from pilha_ligada import Stack

pilha = Stack()
while True:
    valor = int(input('Valor inteiro (<0 para sair): '))
    if valor < 0:
        break
    pilha.push(valor)

    print(f'Pilha tem {pilha.__len__()} itens')

    print(f'Item do topo: {pilha.peek()}')

while not pilha.isEmpty():
    nodo = pilha.pop()
    print(nodo)

print(f'Pilha tem {pilha.__len__()} itens')