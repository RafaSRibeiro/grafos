from Vertice import Vertice
from Aresta import Aresta
from collections import defaultdict


class Grafo(object):

    def __init__(self, vertices=[], arestas=[], orientado=True):
        self.orientado = orientado
        self.vertices = []
        id = 0
        for vertice in vertices:
            self.vertices.append(Vertice(id, vertice))
            id += 1

        self.arestas = []
        id = 0
        for origem, destino in arestas:
            self.addAresta(id, origem, destino)
            id += 1

    def addVertice(self, id):
        # string = input(str("Identificador do Vertice: "))
        self.vertices.append(Vertice(id))

    def addAresta(self, id, origem, destino, peso=0):
        origem = self.findVerticeByRotulo(origem)
        destino = self.findVerticeByRotulo(destino)
        if (origem is not None) and (destino is not None):
            self.arestas.append(Aresta(id, origem, destino, peso))
        else:
            print("Vertice %s ou %s não existe" % (origem, destino))

        if self.orientado == False:
            self.arestas.append(Aresta(id, destino, origem, peso))

    def findVerticeByRotulo(self, rotulo):
        for vertice in self.vertices:
            if rotulo == vertice.rotulo:
                return vertice
        else:
            return None

    def listaAdjacencia(self):
        listaAdjacente = defaultdict(set)
        for aresta in self.arestas:
            listaAdjacente[aresta.origem].add(aresta.destino)
            if not self.orientado:
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

    def imprimeListaArestas(self):
        for aresta in self.arestas:
            if self.orientado:
                separador = "=>"
            else:
                separador = "<=>"
            print(aresta.origem, separador, aresta.destino)

    def listaMatrizIncidencia(self):
        quantidadeVertices = len(self.vertices)
        quantidadeArestas = len(self.arestas)
        matriz = [[' 0' for col in range(quantidadeArestas)] for row in range(quantidadeVertices)]
        for vertice in self.vertices:
            for aresta in self.arestas:
                if vertice.id in (aresta.origem.id, aresta.destino.id):
                    if self.orientado:
                        matriz[vertice.id][aresta.id] = '-1'
                        matriz[aresta.id][vertice.id] = ' 1'
                    else:
                        matriz[vertice.id][aresta.id] = ' 1'
        return matriz

    def imprimeMatrizAdjacencia(self):
        matriz = self.listaMatrizAdjacencia()
        print(' ', end="|", flush=True)
        for vertice in self.vertices:
            print(vertice.rotulo, end="|", flush=True)
        print('')
        tamanhoVertices = len(self.vertices)
        for i in range(0, tamanhoVertices):
            vertice = g.vertices[i]
            print(vertice.rotulo, end="|", flush=True)
            for j in range(0, tamanhoVertices):
                print(matriz[i][j], end="|", flush=True)
            print('')

    def imprimeMatrizIncidencia(self):
        matriz = self.listaMatrizIncidencia()
        print(' ', end="|", flush=True)
        for aresta in self.arestas:
            print('', aresta.origem, aresta.destino, end="|", flush=True)
        print('')
        quantidadeVertices = len(self.vertices)
        quantidadeArestas = len(self.arestas)
        for i in range(0, quantidadeVertices):
            vertice = self.vertices[i]
            print(vertice.rotulo, end="|", flush=True)
            for j in range(0, quantidadeArestas):
                print(' ', matriz[i][j], end="|", flush=True)
            print('')

    def imprimeListaAdjacencia(self):
        listaAdjacencia = self.listaAdjacencia()
        for origem, destinos in listaAdjacencia.items():
            print(origem, end=" => ", flush=True)
            for destino in destinos:
                print(destino, end=",", flush=True)
            print()


vertices = ['A', 'B', 'C', 'D', 'E', 'F']
arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]

g = Grafo(vertices, arestas, True)
print(g.imprimeListaArestas())
print(g.imprimeListaAdjacencia())
print(g.imprimeMatrizAdjacencia())
print(g.imprimeMatrizIncidencia())