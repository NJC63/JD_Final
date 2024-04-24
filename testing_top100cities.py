import pandas as pd


df = pd.read_csv("top100cities.csv")
df["city"] = df["city"].str.lower()
df["state"] = df["state"].str.lower()


#city = input("Please enter your city:").lower()
city = "richmond"
state = "virginia"




# Checking for if the value is in the top 100 most populous cities

inTop100 = False
location = -1
i = 0

val = df["city"] == city
valState = df["state"] == state
while (i < 100):
    if((val[i] == True) & (valState[i] == True)):
        inTop100 = True
        location = i
    i += 1

if(inTop100 == False):
    exit()



row = df.iloc[[location]]


state = str((row["state"])[location])
population = str((row["population_2020"])[location])
largestCityInState = str((row["largest_city_in_state"])[location])
stateCapital = str((row["state_capital"])[location])
federalCapital = str((row["federal_capital"])[location])



city = city.title()

print("Your city is in the top 100 most populous cities within the United States.")
print("According to the 2020 census " + city + " has " + population + " people.")

print(city + " is ranked as the number " + str(location + 1) + " most populous city within the U.S.")

if(largestCityInState == True): print(city + " is the largest city within " + state.title() + ".")
if(stateCapital == True): print(city + " is the state capital in " + state.title() + ".")
if(federalCapital == True): print(city + " is the federal capital.")
    