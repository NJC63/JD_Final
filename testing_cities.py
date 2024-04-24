import pandas as pd


df = pd.read_csv("cities.csv")

df["city"] = df["city"].str.lower()
df["st"] = df["st"].str.lower()
df["state"] = df["state"].str.lower()


# city = input("City: ").lower()
# state = input("State: ").lower()
city = "cleveland"
state = "ohio"

row_for_city = df[df["city"] == city]
states = row_for_city["state"].tolist()


i = 0
while(i < len(states)):
    if(states[i] == state):
        row = row_for_city.iloc[[i]]
    i += 1

st = row["st"]
county = row["county"]
zip = row["zip"]
index = (row.index)[0]



print(city.title() + " is in the state " + state.title() + " with initials " + str(st[index]).upper() + ".")
print("County for " + city.title() + " is " + str(county[index]).title() + " County .")
print("Zip for " + city.title() + " is " + str(zip[index]) + ".")