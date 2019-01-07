from Compteur import Compteur
from User import User
from Consommation import Consommation
import redis

class Extractor:
	def __init__(self):
		self.r = redis.Redis(host='localhost',port=6379,charset='utf-8',decode_responses=True)
		self.__getData()

	def __getData(self):
		self.users = self.__getUsers()

	def __getUsers(self):
		users = []
		userIds = userIds = self.r.lrange('Users',0,100)#['AMAZZAL','JABBEUR','REFAK']
		for userId in userIds:
			users.append(self.__getUserById(userId))
		return users
	def __getUserById(self,userId):
		userDetails = self.r.hgetall(userId)#{'name':userId,'cat':'Home'}
		id = userId
		cat = userDetails['cat']
		name = userDetails['name']
		compteurs = self.__getCompteursByUserId(userId)
		user = User(id,name,cat,compteurs)
		return user
	def __getCompteursByUserId(self,userId):
		compteursIds = self.r.lrange(userId+'Compteurs',0,100)#['MAC0','MAC1']
		compteurs = []
		for compteurId in compteursIds:
			compteurs.append(self.__getCompteurById(compteurId))
		return compteurs

	def __getCompteurById(self,compteurId):
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
	def logAll(self):
		for user in self.users:
			user.log()

	def getUserById(self,userId):
		for user in self.users:
			if user.id==userId:
				return user
		return None
	def getCompteurById(self,user,compteurId):
		for compteur in user.compteurs:
			if compteur.id==compteurId:
				return compteur
		return None
	def calculateByUser(self,user,dateStart,dateEnd):
		valeur = 0.0
		for compteur in user.compteurs:
			valeur += self.calculateByCompteur(compteur,dateStart,dateEnd)
		return valeur
	def calculateByCompteur(self,compteur,dateStart,dateEnd):
		valeur = 0.0
		for consommation in compteur.consommations:
			if dateStart==None or dateEnd==None or consommation.date>=dateStart and consommation.date<=dateEnd:
				valeur += float(consommation.valeur)
		return valeur
