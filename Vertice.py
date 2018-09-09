class Vertice():
    def __init__(self, id, rotulo):
        self.id = id
        self.rotulo = rotulo

    def __str__(self):
        return "%s" % (self.rotulo)

    def __repr__(self):
        return "%s" % (self.rotulo)