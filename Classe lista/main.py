from list_seq import Lista

L = Lista()

menu = """EDITOR DE LISTAS
1 - EXIBIR LISTA
2 - INSERIR
3 - REMOVER
4 - EXIBIR ELEMENTO
5 - EXIBIR POSIÇÃO
6 - ESVAZIAR
0 - SAIR
DIGITE SUA OPÇÃO: """

while True:
    op = int(input(menu))
    if op == 1:   
        L.exibir()
    elif op == 2:
        val = int(input('Informe o valor: '))
        pos = int(input('Informe a posição: '))
        if pos >= 0:
            L.inserir(val, pos)
        else:
            print('Posição inválida!')
    elif op == 3:
        pos = int(input('Informe o índice: '))
        if pos <= L.n:
            L.remover(pos)
        else:
            print('Índice inválido')
    elif op == 4:
        pos = int(input('Informe o Índice: '))
        if pos <= L.n:
            L.ex_elemento(pos)
        else:
            print('Índice inválido')
    elif op == 5:
        val = int(input('Informe o Elemento: '))
        if val in L.itens:
            L.ex_posicao(val)
        else:
            print('Valor inexistente')

    elif op == 6:
        L.esvaziar()
    elif op == 0:
        break
    else:
        continue