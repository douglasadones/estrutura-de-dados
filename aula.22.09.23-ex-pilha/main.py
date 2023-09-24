from pilha_sequencial import Stack
# from pilha_ligada import Stack  ## Se usar esse, agora estamos usando a ligada, sem precisar mudar nada do main.py Se usar esse

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

# infixa (A+B), prefixa (+AB), posfixada (AB+). O computador usa essa última opção.

# Procurar questão da maratona de programação pra treinar pilha: Botas perdidas