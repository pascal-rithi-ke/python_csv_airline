import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

PathData = ["csv/airlines.csv","csv/airports.csv","csv/flights.csv","csv/weather.csv","csv/planes.csv"]
NomTable = ['airline','airport','vol','meteo','avion']

def SetupBdd():
    engine = create_engine("mysql+pymysql://{user}:{pw}@mysql-airport.alwaysdata.net/{db}"
                       .format(user="airport",
                               pw="PascalAdrienBisou77",
                               db="airport_projet_csv"))
    for index, element in enumerate(PathData):
        data = pd.read_csv(PathData[index])
        data.to_sql(NomTable[index], con = engine, if_exists = 'replace', chunksize = 1000)




# Question1 (1)
#Nombre d'aéroports
TotalAirport = pd.read_csv(PathData[1])
print('Nombre total aéroport')
print(TotalAirport['faa'].count())
     

# Question1 (1)
#Nombre de départ & destination
DepartDestination = pd.read_csv(PathData[2])
print('Nombre total de départ et de destination')
print(DepartDestination['origin'].count())
print(DepartDestination['dest'].count())


# Question1 
#Nombre de compagnie
TotalAirline = pd.read_csv(PathData[0])
print('Nombre total de compagnies')
print(TotalAirline['name'].count())

#Nombre d'avions
TotalAvion = pd.read_csv(PathData[4])
print('Nombre total avions')
print(TotalAvion['tailnum'].count())

# Question1 (2)
# Nombre aéroport Etats Unis de Passage Heure été Hiver
def Passage_Heure_ete_hiver():
     print('Passage heure été/hiver')
     print(pd.read_csv(PathData[1]).dst.value_counts()[2])
Passage_Heure_ete_hiver()


# Question1 (2)
# Nombre de fuseaux horaire
def Fuseaux_Horaire():
     print('Nombre de Fuseaux Horaire')
     print(pd.read_csv(PathData[1]).tzone.value_counts())
Fuseaux_Horaire()

# Question1 (3)
#Nombre de vols annulés
TotalVolAnnule = pd.read_csv(PathData[2])
print('Nombre de vols annulés')
print(TotalVolAnnule.loc[TotalVolAnnule['dep_time'] == " "].shape[0])


# Question2 (1)
# Aeroport le plus emprunté
def Aeroport_Plus_Emprunter():
     print('Nombre daéroport le plus emprunté')
     print(pd.read_csv(PathData[2]).origin.value_counts().nlargest())
Aeroport_Plus_Emprunter()

# Question2 (2)
# Déstination les plus prisées
def Destination_Prisees():
     print('Destination les plus prisées')
     print(pd.read_csv(PathData[2]).dest.value_counts(normalize=True).nlargest(n=10)*100)
Destination_Prisees()

# Question2 (3)
# Destination les moins prisées
def Destination_Moins_Prisees():
     print('Destination les moins prisées')
     print(pd.read_csv(PathData[2]).dest.value_counts(normalize=True).nsmallest(n=10)*100)
Destination_Moins_Prisees()

# Question (3)
# Combien chaque compagnie a desservie de destination par aéroport d’origine
#Nombre de destination desservi pour chaque compagnie

NombreDestinationComp = pd.read_csv(PathData[2])
print('Combien chaque compagnie a desservie de destination par aéroport d’origine, Nombre de destination desservi pour chaque compagnie')
columns = NombreDestinationComp['carrier'].value_counts().index.tolist()
dataCol = NombreDestinationComp['carrier'].value_counts().tolist()

#création barre graphique
plt.bar(columns,dataCol)

plt.xlabel("Nom des compagnies")
plt.ylabel("Nombre de destination desservi")
plt.title("Nombre de destination desservi pour chaque compagnie")
plt.show()

print("***********")
NombreDestinationComp = pd.read_csv(PathData[2])
columns = NombreDestinationComp['carrier'].value_counts().index.tolist()
dataCol = NombreDestinationComp['carrier'].value_counts().tolist()

# création barre graphique
plt.bar(columns,dataCol)

plt.xlabel("Nom des compagnies")
plt.ylabel("Nombre de destination desservi")
plt.title("Nombre de destination desservi pour chaque compagnie")
plt.show()
