from list_ligada import Lista


def principal():
    lista = Lista()
    while True:
        valor = int(input("Informe o valor: "))
        if valor == 0:
            break
        lista.inserir(valor)

    lista.mostrar()
    lista.limpar()
    print(f'Lista após apagar o endereço: {lista.mostrar()}')

principal()
