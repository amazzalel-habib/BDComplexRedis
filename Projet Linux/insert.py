import redis

r = redis.Redis(host='localhost',port=6379,charset='utf-8',decode_responses=True)

r.flushall()
users = {
	'AMAZZAL':{'name':'AMAZZAL EL-HABIB','cat':'personnel'},
	'JABBEUR':{'name':'JABBEUR Youssef','cat':'personnel'},
	'REFAK':{'name':'REFAK Aymane','cat':'personnel'},
	'BERRADA':{'name':'BERRADA Omar','cat':'Hôpital'}
}
userCompteur = {
	'AMAZZALCompteurs':['COM1','COM2'],
	'JABBEURCompteurs':['COM3'],
	'REFAKCompteurs':['COM4'],
	'BERRADACompteurs':['COM5']
}
compteursDetails = {
	'COM1Adresse':'Avenue X 61 RABAT',
	'COM2Adresse':'Avenue A 54 RABAT',
	'COM3Adresse':'Avenue C 58 CASA',
	'COM4Adresse':'Avenue R 84 RABAT',
	'COM5Adresse':'Avenue Z 2 CASA'
}
compteurConsommation = {
	'COM1':['2018-05-01 10:00:00.000000',0.5,'2018-05-01 10:30:00.000000',0.6,'2018-05-01 11:00:00.000000',0.1,'2018-05-02 10:00:00.000000',0.3],
	'COM2':['2018-05-01 10:00:00.000000',0.5],
	'COM3':['2018-05-01 10:00:00.000000',0.5],
	'COM4':['2018-05-01 10:00:00.000000',0.5],
	'COM5':['2018-05-01 10:00:00.000000',0.5]
}
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
