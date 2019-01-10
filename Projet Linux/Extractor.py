from Compteur import Compteur
from User import User
from Consommation import Consommation
import redis

"""
Ce module permet d'extraire les données
"""

class Extractor:
	def __init__(self):
		"""
			Cete méthode sert à se connecter au serveur Redis
			et récupère les données 
		"""
		self.r = redis.Redis(host='localhost',port=6379,charset='utf-8',decode_responses=True)
		self.__getData()

	def __getData(self):
		"""
		Récupèrer les données de tous les utilisateurs, les compteurs et les consommation
		self.users : contient une liste des utilisateurs de type User
		
		"""
		self.users = self.__getUsers()

	def __getUsers(self):
		users = []
		"""
			Récupére la liste des IDs de tous les clients
			sous fomre: ['AMAZZAL','JABBEUR','REFAK']
			puis récupérer les données concernant chacun par son ID
		"""
		userIds = userIds = self.r.lrange('Users',0,100)
		for userId in userIds:
			#Pour chaque ID d'un client récupére ses details par cet ID
			users.append(self.__getUserById(userId))
		return users
	def __getUserById(self,userId):
		"""
		Récupérer un client par son ID
		"""
		userDetails = self.r.hgetall(userId)#{'name':userId,'cat':'Home'}
		id = userId
		cat = userDetails['cat']
		name = userDetails['name']
		compteurs = self.__getCompteursByUserId(userId)
		user = User(id,name,cat,compteurs)
		return user
	def __getCompteursByUserId(self,userId):
		"""
			Récupére la liste des compteurs d'un client par son ID
		"""
		compteursIds = self.r.lrange(userId+'Compteurs',0,100)#['MAC0','MAC1']
		compteurs = []
		for compteurId in compteursIds:
			compteurs.append(self.__getCompteurById(compteurId))
		return compteurs

	def __getCompteurById(self,compteurId):
		"""
			récupère les details d'un compteur par son ID
		"""
		adresse = self.r.get(compteurId+'Adresse')#"Adresse rabat"
		cons = self.r.lrange(compteurId,0,100)#['2012-10-12 10:00:00.0000000',0.2,'2012-10-12 10:30:00.0000000',0.6]
		consommations = []
		for i in range(0,len(cons)-2,2):
			date = cons[i+1]
			valeur = cons[i]
			consommation = Consommation(date,valeur)
			consommations.append(consommation)
		compteur = Compteur(compteurId,adresse,consommations)
		return compteur
	def getUserById(self,userId):
		"""
		Permet de récupèrer le client par son ID
		"""
		for user in self.users:
			if user.id==userId:
				return user
		return None
	def getCompteurById(self,user,compteurId):
		"""
		Permet de récupèrer le compteur par son ID
		"""
		for compteur in user.compteurs:
			if compteur.id==compteurId:
				return compteur
		return None
	def calculateByUser(self,user,dateStart,dateEnd):
		"""
		Permet de calculer la consommation moyenne d'un utilisateur
		pour tous ses compteurs dans 
		une intervalle données [dateStart,dateEnd]
		la valeur retourner est en KWH
		"""
		valeur = 0.0
		for compteur in user.compteurs:
			valeur += self.calculateByCompteur(compteur,dateStart,dateEnd)
		return valeur
	def calculateByCompteur(self,compteur,dateStart,dateEnd):
		"""
		Permet de calculer la consommation moyenne pour un compteur dans 
		une intervalle données [dateStart,dateEnd]
		la valeur retourner est en KWH
		"""
		valeur = 0.0
		for consommation in compteur.consommations:
			if dateStart==None or dateEnd==None or consommation.date>=dateStart and consommation.date<=dateEnd:
				valeur += float(consommation.valeur)
		return valeur
