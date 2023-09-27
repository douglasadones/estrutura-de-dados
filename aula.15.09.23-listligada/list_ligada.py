class No():
    def __init__(self, info):
        self.info = info
        self.prox = None  # "Ponteiro"

    def get_info(self):
        return self.info


class Lista:
    def __init__(self):
        self.prim = None
        self.tamanho = 0

    def estaVazia(self):
        return self.tamanho == 0

    def percorrer(self):  # lógica para percorrer a lista ligada.
        temp = self.prim
        while temp is not None:
            # Realizar a operação devida com o temp.info
            temp = temp.prox

    def mostrar(self):  # mostra todos os elementos da lista
        temp = self.prim
        while temp is not None:
            print(temp.info, end=' ')
            temp = temp.prox

    def buscar(self, value):  # retorna o nó cuja informação contida é a informada no param. value
        temp = self.prim
        while temp is not None and temp.info != value:
            temp = temp.prox
        if temp is not None:
            return temp
        return None

    def inserir(self, valor, pos=None):
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

    def val_remover(self, value):
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

    def limpar(self):
        temp = self.prim
        while temp is not None:
            self.prim = temp.prox
            temp = temp.prox
        self.tamanho = 0







# class Lista:  # Da aula que faltei
#     def __init__(self):
#         self.prim = None
#         self.tamanho = 0
#
#     def inserir(self, valor):  # Pelo que entendi, a "ordem" é inversa nessa lista ligada.
#         novo = No(valor)
#         novo.prox = self.prim  # nó inserido aponta para o primeiro nó da lista Obs: o primeiro inserido n aponta para ninguem(None).
#         self.prim = novo  # O primeiro elemento da lista sempre será o último adicionado
#         self.tamanho += 1
#
#     def mostrar(self):
#         atual = self.prim  # Primeiro nó da lista (último adicionado) como ponto de partida.
#         while atual is not None:  # enquanto não chegar no primeiro nó adicionado.
#             print(atual.info, end=" ")  # Mostra a info do nó atual
#             atual = atual.prox  # o atual vira o nó no qual ele estava apontando. (Note que estamos indo do fim para o começo).
#
#     def buscar(self, valor):
#         atual = self.prim  # O primeiro elemento da lista (ultimo adicionado) é usado para percorrer a lista.
#         while atual is not None:
#             if atual.info == valor:
#                 return True
#             atual = atual.prox
#         return False
