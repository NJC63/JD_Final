import pandas as pd


df = pd.read_csv("airports.csv")

df["CITY"] = df["CITY"].str.lower()
df["STATE"] = df["STATE"].str.lower()
df["COUNTRY"] = df["COUNTRY"].str.lower()

# city = input("Please enter your city:").lower()
city = "cleveland"
st = "oh"



inAirports = False
location = -1
i = 1

val = df["CITY"] == city
valSt = df["STATE"] == st
while (i <= 340):
    if((val[i] == True) & (valSt[i] == True)):
        inAirports = True
        location = i
    i += 1

if(inAirports == False):
    exit()


row = df.iloc[[location]]


airport = str((row["AIRPORT"])[location])
iata = str((row["IATA"])[location])


print("The main airport for " + city.title() + " is " + airport + " Airport.")
print("The IATA code for " + airport + " is " + iata + ".")
