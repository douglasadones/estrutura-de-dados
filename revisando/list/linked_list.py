class No():
    def __init__(self, info):
        self.info = info
        self.prox = None  # "Ponteiro"


class Lista:
    def __init__(self):
        self.prim = None
        self.tamanho = 0

    def isEmpty(self):
        return self.tamanho == 0

    def walk_through_escheme(self):  # lógica para percorrer a lista ligada.
        temp = self.prim
        while temp is not None:
            # Realizar a operação devida com o temp.info
            temp = temp.prox

    def show(self):  # mostra todos os elementos da lista
        temp = self.prim
        while temp is not None:
            print(temp.info, end=' ')
            temp = temp.prox

    def search(self, value):  # retorna o nó cuja informação contida é a informada no param. value
        temp = self.prim
        while temp is not None and temp.info != value:
            temp = temp.prox
        if temp is not None:
            return temp
        return None

    def insert(self, valor, pos=None):
        novo = No(valor)
        if pos is None:  # Inserir no início
            novo.prox = self.prim
            self.prim = novo
        else:
            temp = self.prim  # No atual dos loops/ponto de partida
            if pos == self.tamanho:  # adicionar no final como um "append":
                while temp.prox is not None:
                    temp = temp.prox
                temp.prox = novo
            else:  # adicionar em qualquer outra posição. Aqui o temp vira o nó anterior
                pos_atual = 0
                while pos_atual != pos-1:  # pos-1 para parar no nó anterior (e obter acesso ao nó anterior e posterior)
                    temp = temp.prox
                    pos_atual += 1
                novo.prox = temp.prox  # Novo nó adicionado apontando para o nó seguinte
                temp.prox = novo  # Nó anterior apontando para o novo nó adicionado
        self.tamanho += 1

    def remove_value(self, value):
        """Remove um nó a partir de seu value"""
        atual = self.prim
        anterior = None
        while atual is not None and atual.info != value:
            anterior = atual
            atual = atual.prox
        if atual is not None and atual.info == value:
            if atual == self.prim:  # caso seja na primeira posição
                self.prim = self.prim.prox
            else:
                anterior.prox = atual.prox  # Atenção para a lógica aqui
            self.tamanho -= 1
            return atual
        return None

    def clear(self):
        temp = self.prim
        while temp is not None:
            self.prim = temp.prox
            temp = temp.prox
        self.tamanho = 0