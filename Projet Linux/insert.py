import redis
import random as rd
from datetime import datetime,timedelta

#Se connecter au serveur Redis
r = redis.Redis(host='localhost',port=6379,charset='utf-8',decode_responses=True)
# Suprimmer toutes les données avant d'insérer de nouvelles données
r.flushall()
#Nombre du client à générer
numOfUsers = 100
# nombre de compteur par client à générer
numOfCompteurPerClient = 5
#La liste des utilisateur identifiés par leurs ID
users = {}
#la liste des compteur identifié par le client
userCompteur = {}
# les details de chaque client
compteursDetails = {}
# la liste des consommations pour chaque compteur
compteurConsommation = {}
#Commencer à générer les données aléatoirement
for i in range(numOfUsers):
	#Générer les utilisateur
	id = 'Nom'+str(i+1)
	user = {'name':id,'cat':'Personnel'}
	users[id] = user

for i in range(numOfUsers):

	id = 'Nom'+str(i+1)+'Compteurs'
	#Générer les compteurs
	compteurs = ['COM'+str(i+1)+'-'+str(j+1) for j in range(numOfCompteurPerClient)]
	userCompteur[id] = compteurs
	for j in range(numOfCompteurPerClient):
		compteurID = 'COM'+str(i+1)+'-'+str(j+1)
		#Générer les details de chaque compteur
		compteursDetails[compteurID+'Adresse'] = 'Avenue X '+str(i+1)+str(j+1)+' RABAT'
		numOfCons = rd.randint(10,100)
		dateNow = datetime.now()
		startDate = dateNow-timedelta(days=5)
		consommations = []
		for _ in range(numOfCons):
			#Générer les consommation pour chaque compteur d'une façon aléatoire
			date = startDate + timedelta(minutes=30)
			valeur = float('{:.2f}'.format(rd.random()*10))
			startDate = date
			consommations.append(date.strftime('%Y-%m-%d %H:%M:%S.%f'))
			consommations.append(valeur)
		compteurConsommation[compteurID] = consommations

#Inserer les utilisateur IDS
r.lpush('Users',*tuple(users.keys()))


for key in users.keys():
	#Inserer les details de chaque client
	r.hmset(key,users.get(key))
for key in compteursDetails.keys():
	#Inserer les details de chaque compteur
	r.set(key,compteursDetails.get(key))
for key in userCompteur.keys():
	#Inserer les compteurs de chaque client
	r.lpush(key,*tuple(userCompteur.get(key)))
for key in compteurConsommation.keys():
	#Inserer les consommations de chaque compteurs
	r.lpush(key,*tuple(compteurConsommation.get(key)))
