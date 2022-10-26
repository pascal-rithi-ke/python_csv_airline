import pandas as pd

CheminAirline = " csv/airlines.csv"
CheminAeroport ="csv/airports.csv"
CheminVols = "csv/flights.csv"
CheminMeteo = "csv/weather.csv"
CheminAvions = " csv/planes.csv"

def TotalAirport():
    TotalAirport = pd.read_csv(CheminAeroport)
    return print(len(TotalAirport))


def DepartDestination():
    DepartDestination = pd.read_csv(CheminVols)
    return print(len(DepartDestination))