class Casa:
    
	def __init__(self, preco):
		self._preco = preco

	@property
	def preco(self):
		return self._preco
	
	@preco.setter
	def preco(self, new_price):
		if novo_preco > 0 and isinstance(novo_preco, float):
			self._preco = novo_preco
		else:
			print("Insira um preço válido")

	@preco.deleter
	def preco(self):
		del self._preco