
class User:
	def __init__(self,id,name,cat,compteurs):
		self.id = id
		self.name = name
		self.cat = cat
		self.compteurs = compteurs

	def log(self):
		print('User id: ',self.id)
		print('User Name: ',self.name)
		print('User Compeurs: ')
		for compteur in self.compteurs:
			compteur.log()
			print('_____________')
		print('--------------------------------------------')

	def __str__(self):
		return self.name