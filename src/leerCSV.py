import csv

class Municipio:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def increment(self,quantity):
        self.quantity += quantity



municipios =  []
with open('./data/cm.csv', newline='', encoding='iso-8859-1') as csvfile:
    next(csvfile)
    spamreader = csv.reader(csvfile,delimiter=';', quotechar='|')
    for row in spamreader:
        municipioTmp = Municipio(row[1],row[4])
        
        for municipio in municipios:
            print(municipio)
            if(municipio.name == row[1]):
                municipio.increment(row[4])
            else:
                municipios.append(municipioTmp)

        #if(any(municipio.name == row[1] for municipio in municipios)):
        #    municipios
        #else:
        #    municipios.append(municipioTmp)
            
        #if(municipios.count(row[1])==0):
        #    municipios.append( row[1] )

print(municipios)