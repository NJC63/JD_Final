import pandas as pd


df = pd.read_csv("cities.csv")

df["city"] = df["city"].str.lower()
df["st"] = df["st"].str.lower()
df["state"] = df["state"].str.lower()


# city = input("City: ").lower()
# state = input("State: ").lower()
city = "cleveland"
state = "ohio"


val = df["city"] == city

inCities = False
location = -1
i = 1

if(len(state) == 2):
    valSt = df["st"] == state
    while (i <= 19501):
        if((val[i] == True) & (valSt[i] == True)):
            inCities = True
            location = i
        i += 1

else:
    valState = df["state"] == state
    while (i <= 19501):
        if((val[i] == True) & (valState[i] == True)):
            inCities = True
            location = i
        i += 1


if(inCities == False):
    print("Your city and state do not appear to be in the US database.")
    exit()

row = df.iloc[[location]]

st = row["st"]
state = row["state"]
county = row["county"]
zip = row["zip"]
index = (row.index)[0]

print(city.title() + " is in the state " + str(state[index]).title() + " with initials " + str(st[index]).upper() + ".")
print("County for " + city.title() + " is " + str(county[index]).title() + " County .")
print("Zip for " + city.title() + " is " + str(zip[index]) + ".")