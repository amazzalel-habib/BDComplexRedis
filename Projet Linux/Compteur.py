"""
	Classe Compteur (Model)
"""
class Compteur:
	def __init__(self,id,adresse,consommations):
		self.id = id
		self.adresse = adresse
		self.consommations = consommations

	def log(self):
		print('\tCompteur ID: ',self.id)
		print('\tConsommations:')
		for cons in self.consommations:
			cons.log()

	def __str__(self):
		return self.id