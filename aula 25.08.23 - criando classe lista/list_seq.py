class Lista:
    def __init__(self):
        self.itens = [1, 3, 5]
        self.n = 3

    def exibir_lista(self):
        if self.n == 0:
            print('[]')
        else:
            print('[', end='')
            for i, item in enumerate(self.itens):
                print(item, end=', ' if i != self.n - 1 else ']')


    def inserir(self, pos, val):
        if self.n == 0:
            self.itens += [val]
        else:
            self.itens += ['x']
            for i, item in enumerate(self.itens):





            self.itens += [val]
        self.n += 1

