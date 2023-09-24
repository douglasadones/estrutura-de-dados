class No():
    def __init__(self, info):
        self.info = info
        self.prox = None  # "Ponteiro"
    
    def get_info(self):
        return self.info


class Lista():
    def __init__(self):
        self.prim = None
        self.tamanho = 0

    def inserir(self, valor):  # Pelo que entendi, a "ordem" é inversa nessa lista ligada.
        novo = No(valor)  
        novo.prox = self.prim  # nó inserido aponta para o primeiro nó da lista Obs: o primeiro inserido n aponta para ninguem(None).
        self.prim = novo # O primeiro elemento da lista sempre será o último adicionado
        self.tamanho += 1
    
    def mostrar(self):
        atual = self.prim  # Primeiro nó da lista (último adicionado) como ponto de partida.
        while atual is not None:  # enquanto não chegar no primeiro nó adicionado.
            print(atual.info, end=" ")  # Mostra a info do nó atual
            atual = atual.prox  # o atual vira o nó no qual ele estava apontando. (Note que estamos indo do fim para o começo).
    
    def buscar(self, valor):
        atual = self.prim  # O primeiro elemento da lista (ultimo adicionado) é usado para percorrer a lista.
        while atual is not None:   
            if atual.info == valor:
                return True
            atual = atual.prox
        return False



def principal():
    lista = Lista()
    while True:
        valor = int(input("Informe o valor: "))
        if valor == 0: break
        lista.inserir(valor)

    lista.mostrar()


if __name__ == "__main__":
    principal()