import pandas as pd


df = pd.read_csv("top100cities.csv", index_col=0)
df["city"] = df["city"].str.lower()
df["state"] = df["state"].str.lower()


city = input("Please enter your city:").lower()



row_for_city = df[df["city"] == city]
state = row_for_city["state"]
population = row_for_city["population_2020"]
largestCityInState = row_for_city["largest_city_in_state"]
stateCapital = row_for_city["state_capital"]
federalCapital = row_for_city["federal_capital"]




# Checking for if the value is in the top 100 most populous cities
val = df["city"] == city

inTop100 = False
location = -1
i = 1
while (i <= 100):
    if(val[i] == True):
        inTop100 = True
        location = i
    i = i + 1



if(inTop100):

    city = city.title()

    print("Your city is in the top 100 most populous cities within the United States.")
    print("According to the 2020 census " + city + " has " + str(population[location]) + " people.")

    print(city + " is ranked as the number " + str(location) + " most populous city within the U.S.")

    if(largestCityInState[location] == True): print(city + " is the largest city within " + state[location].title() + ".")
    if(stateCapital[location] == True): print(city + " is the state capital in " + state[location].title() + ".")
    if(federalCapital[location] == True): print(city + " is the federal capital.")
    