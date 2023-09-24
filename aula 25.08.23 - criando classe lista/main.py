from list_seq import Lista

menu = """\nEDITOR DE LISTAS
1 - EXIBIR LISTA
2 - INSERIR
3 - REMOVER
4 - EXIBIR ELEMENTOS
5 - EXIBIR POSIÇÃO
6 - ESVAZIAR
0 - SAIR

DIGITE SUA OPÇÃO: """

L = Lista()

while True:
    op = int(input(menu))
    if op == 1:
        L.exibir_lista()
    elif op == 2:
        pos = int(input('Posição: '))
        valor = int(input('valor: '))
        L.inserir(pos, valor)
    elif op == 3:
        pass
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
    elif op == 0:
        break
    else:
        continue
    print()




