from datetime import datetime
"""
	Classe Consommation (Model)
"""
class Consommation:
	def __init__(self,date,valeur):
		datetime_object = self.parse_prefix(date, '%Y-%m-%d %H:%M:%S.%f')
		self.date = datetime_object
		self.valeur = valeur

	def log(self):
		print('\t\tDate:'+ str(self.date))
		print('\t\tValeur:', self.valeur)
		print('')
	def parse_prefix(self,line, fmt):
		cover = len(datetime.now().strftime(fmt))
		return datetime.strptime(line[:cover], fmt)