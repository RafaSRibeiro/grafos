from Grafo import Grafo

valorado = True if input("Grafo valorado (Padrão: Não): (Sim|Não)") == 'Sim' else False
orientado = True if input("Grafo orientado (Padrão: Não): (Sim|Não)") == 'Sim' else False
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
  if valorado:
    aresta.append(arestaArray[1])
  arestas.append(aresta)


g1 = Grafo(vertices, arestas, orientado, valorado)
print("Lista de Arestas")
print(g1.imprimeListaArestas())
print("Lista de Adjacencia")
print(g1.imprimeListaAdjacencia())
print("Matriz de Adjacencia")
print(g1.imprimeMatrizAdjacencia())
print("Matriz de Incidência")
print(g1.imprimeMatrizIncidencia())
