import csv
from pymongo import MongoClient

client = MongoClient()
client = MongoClient(host="172.20.0.6", port=27017,username="root",password="example")
db = client.defunciones
municipios = db.municipio


with open('data/cm.csv', newline='', encoding='iso-8859-1') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    cont = 0
    for row in spamreader:
        if(cont==1):
            print(', '.join(row))
            municipio = {"name":row}
            result = municipios.insert_one(municipio)
        cont = cont + 1
