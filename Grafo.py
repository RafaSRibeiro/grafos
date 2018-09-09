from Vertice import Vertice
from Aresta import Aresta
from collections import defaultdict


class Grafo(object):

    def __init__(self, vertices=[], arestas=[], direcionado=True):
        self.direcionado = direcionado
        self.vertices = []
        id = 0
        for vertice in vertices:
            self.vertices.append(Vertice(id, vertice))
            id += 1

        self.arestas = []
        for aresta in arestas:
            self.addAresta(aresta[0], aresta[1])

    def addVertice(self, id):
        # string = input(str("Identificador do Vertice: "))
        self.vertices.append(Vertice(id))

    def addAresta(self, origem, destino, peso=0):
        origem = self.findVerticeByRotulo(origem)
        destino = self.findVerticeByRotulo(destino)
        if (origem is not None) and (destino is not None):
            self.arestas.append(Aresta(origem, destino, peso))
        else:
            print("Vertice não existe")

        if self.direcionado == False:
            self.arestas.append(Aresta(destino, origem, peso))

    def findVerticeByRotulo(self, rotulo):
        for vertice in self.vertices:
            if rotulo == vertice.rotulo:
                return vertice
        else:
            return None

    def listaAdjacente(self):
        listaAdjacente = defaultdict(set)
        for aresta in self.arestas:
            listaAdjacente[aresta.origem].add(aresta.destino)
            if not self.direcionado:
                listaAdjacente[aresta.destino].add(aresta.origem)
        return listaAdjacente

    def listaArestas(self):
        return self.arestas

    def listaMatrizAdjacencia(self):
        v = len(self.vertices)
        matriz = [[0 for col in range(v)] for row in range(v)]
        for aresta in self.arestas:
            matriz[aresta.origem.id][aresta.destino.id] = 1
        return matriz

    def imprimeMatrizAdjacencia(self):
        matriz = self.listaMatrizAdjacencia()
        print(' ', end="|", flush=True)
        for vertice in g.vertices:
            print(vertice.rotulo, end="|", flush=True)
        print('')
        tamanhoVertices = len(g.vertices)
        for i in range(0, tamanhoVertices):
            vertice = g.vertices[i]
            print(vertice.rotulo, end="|", flush=True)
            for j in range(0, tamanhoVertices):
                print(matriz[i][j], end="|", flush=True)
            print('')

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
arestas = [('A', 'B'), ('A', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]

g = Grafo(vertices, arestas)
g.imprimeMatrizAdjacencia()
