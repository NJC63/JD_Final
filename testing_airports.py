import pandas as pd


df = pd.read_csv("airports.csv")

df["CITY"] = df["CITY"].str.lower()
df["STATE"] = df["STATE"].str.lower()
df["COUNTRY"] = df["COUNTRY"].str.lower()

city = input("Please enter your city:").lower()

row_for_city = df[df["CITY"] == city]

airport = row_for_city["AIRPORT"]
iata = row_for_city["IATA"]



val = df["CITY"] == city
inAirports = False
location = -1
i = 1
while (i <= 100):
    if(val[i] == True):
        inAirports = True
        location = i
    i = i + 1


if(inAirports):

    print("The main airport for " + city.title() + " is " + str(airport[location]) + ".")
    print("The IATA code for " + str(airport[location]) + " is " + str(iata[location]) + ".")
