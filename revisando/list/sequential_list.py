class Lista:
    def __init__(self) -> None:
        self.itens = []
        self.n = 0

    def isEmpty(self) -> bool:
        return self.n == 0

    def show(self):
        for item in self.itens:
            print(item, end=' ')
        print()
        # or
        i = 0
        while i < self.n:
            print(self.itens[i], end=' ')
            i += 1
        print()

    def insert(self, val, pos: int):
        if 0 <= pos < self.n:
            self.itens.insert(pos, val)
        elif pos >= self.n:
            self.itens.append(val)
        self.n += 1

    def clear(self):
        i = 0
        while i < self.n:
            self.itens.pop(0)
            i += 1
        self.n = 0

    def remove(self, pos):
        if not self.isEmpty() and pos < self.n:
            self.n -= 1
            return self.itens.pop(pos)
        else:
            return -1

    def remove_value(self, pos):
        print(self.itens[pos])
        return self.itens[pos]

    def remove_pos(self, valor):
        print(self.itens.index(valor))
        return self.itens.index(valor)
