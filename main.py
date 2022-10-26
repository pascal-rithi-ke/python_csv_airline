import pandas as pd

CheminAirline = "csv/airlines.csv"
CheminAeroport ="csv/airports.csv"
CheminVols = "csv/flights.csv"
CheminMeteo = "csv/weather.csv"
CheminAvions = "csv/planes.csv"


totalAirport = pd.read_csv(CheminAeroport)
print(len(totalAirport))

