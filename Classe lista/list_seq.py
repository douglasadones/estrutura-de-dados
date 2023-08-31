class Lista:
    def __init__(self) -> None:
        self.itens = [1, 2, 3, 4]
        self.n = 4
    
    def lista_vazia(self):
        return self.n == 0
    

    def exibir(self):
        for item in self.itens:
            print(item, end=' ')
        print()
        # ou
        i = 0
        while i < self.n:
            print(self.itens[i], end=' ')
            i += 1
        print()


    def inserir(self, val, pos):
        if pos < self.n:
            self.itens.insert(pos, val)
        else:
            self.itens.append(val)                        
        self.n += 1

    def esvaziar(self):
        i = 0
        while i < self.n:
            self.pop(0)
            i += 1
        self.n = 0

    def remover(self, pos):
        self.itens.pop(pos)
        self.n -= 1

    def ex_elemento(self, pos):
        print(self.itens[pos])
        return self.itens[pos]

    def ex_posicao(self, valor):
        print(self.itens.index(valor))
        return self.itens.index(valor)
