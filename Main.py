from Grafo import Grafo

valorado = True if input("Grafo valorado: (Sim|Não)") == 'Sim' else False or True
orientado = True if input("Grafo orientado: (Sim|Não)") == 'Sim' else False or True

# vertices = ['A', 'B', 'C', 'D', 'E', 'F']
vertices = input("Vertices Ex:A,B,C,D  :")
vertices = vertices.split(",")

# arestas = [('A', 'B', 1), ('B', 'C', 2), ('B', 'D', 3), ('C', 'D', 4), ('E', 'F', 1), ('F', 'C', 1)]
arestasInput = input("Arestas Ex:AB=2,BC=12,BD=9 :")
arestasValorada = arestasInput.split(",")
arestas = []
for arestaValorada in arestasValorada:
  arestaArray = arestaValorada.split("=")
  aresta = []
  aresta.append(arestaArray[0][0])
  aresta.append(arestaArray[0][1])
  aresta.append(arestaArray[1])
  arestas.append(aresta)

# g2 = Grafo(vertices, arestas, True)
# print(g2.imprimeListaArestas())
# print(g2.imprimeListaAdjacencia())
# print(g2.imprimeMatrizAdjacencia())
# print(g2.imprimeMatrizIncidencia())

g1 = Grafo(vertices, arestas, orientado, valorado)
print(g1.imprimeListaArestas())
print(g1.imprimeListaAdjacencia())
print(g1.imprimeMatrizAdjacencia())
print(g1.imprimeMatrizIncidencia())
