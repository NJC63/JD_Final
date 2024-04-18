import pandas as pd


df = pd.read_csv("top100cities.csv", header=0)
df["city"] = df["city"].str.lower()
df["state"] = df["state"].str.lower()


print(df.head(5))


city = input("Please enter your city:")

row_for_city = df[df["city"] == city]
print(row_for_city)


population = row_for_city["population_2020"]

print("Your city is in the top 100 most populous cities in the United States.")
print("According to the 2020 census " + city + " has " + str(population) + "people")









