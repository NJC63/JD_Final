import pandas as pd


df = pd.read_csv("cities.csv")

df["city"] = df["city"].str.lower()
df["st"] = df["st"].str.lower()
df["state"] = df["state"].str.lower()


city = input("Please enter your city:").lower()

row_for_city = df[df["city"] == city]

st = row_for_city["st"]
state = row_for_city["state"]
county = row_for_city["county"]
zip = row_for_city["zip"]


val = df["city"] == city
inCities = False
location = -1
i = 1


while (i <= 19501):
    if(val[i] == True):
        inCities = True
        location = i
    i += 1



if(inCities):
    print(city.title() + " is in the state " + str(state[location]).title() + " with initials " + str(st[location]).upper() + ".")
    print("County for " + city.title() + " is " + str(county[location]).title() + " County .")
    print("Zip for " + city.title() + " is " + str(zip[location]) + ".")