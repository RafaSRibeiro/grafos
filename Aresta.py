class Aresta():
    def __init__(self, id, origem, destino, peso=0):
        self.id = id
        self.origem = origem
        self.destino = destino
        self.peso = peso

    def __str__(self):
        return "(%s,%s)" % (self.origem, self.destino)

    def __repr__(self):
        return "(%s,%s)" % (self.origem, self.destino)
