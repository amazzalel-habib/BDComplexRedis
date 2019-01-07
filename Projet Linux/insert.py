import redis
import random as r
from datetime import datetime,timedelta
r = redis.Redis(host='localhost',port=6379,charset='utf-8',decode_responses=True)

r.flushall()
numOfUsers = 100
numOfCompteurPerClient = 5
users = {}
userCompteur = {}
compteursDetails = {}
compteurConsommation = {}
for i in range(numOfUsers):
	id = 'Nom'+str(i+1)
	user = {'name':id,'cat':'Personnel'}
	users[id] = user

for i in range(numOfUsers):
	id = 'Nom'+str(i+1)+'Compteurs'
	compteurs = ['COM'+str(i+1)+'-'+str(j+1) for j in range(numOfCompteurPerClient)]
	userCompteur[id] = compteurs
	for j in range(numOfCompteurPerClient):
		compteurID = 'COM'+str(i+1)+'-'+str(j+1)
		compteursDetails[compteurID+'Adresse'] = 'Avenue X '+str(i+1)+str(j+1)+' RABAT'
		numOfCons = r.randint(10,100)
		dateNow = datetime.now()
		startDate = dateNow-timedelta(days=5)
		consommations = []
		for _ in range(numOfCons):
			date = startDate + timedelta(minutes=30)
			valeur = float('{:.2f}'.format(r.random()*10))
			startDate = date
			consommations.append(date.strftime('%Y-%m-%d %H:%M:%S.%f'))
			consommations.append(valeur)
		compteurConsommation[compteurID] = consommations

#Inserer les utilisateur IDS
r.lpush('Users',*tuple(users.keys()))

for key in users.keys():
	r.hmset(key,users.get(key))
for key in compteursDetails.keys():
	r.set(key,compteursDetails.get(key))
for key in userCompteur.keys():
	r.lpush(key,*tuple(userCompteur.get(key)))
for key in compteurConsommation.keys():
	r.lpush(key,*tuple(compteurConsommation.get(key)))