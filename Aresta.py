class Aresta():
	def __init__(self,origem,destino,peso = 0):
		self.origem = origem
		self.destino = destino
		self.peso = peso

	def __str__(self):
		return "(%s,%s)" % (self.origem,self.destino)

	def __repr__(self):
		return "(%s,%s)" % (self.origem,self.destino)