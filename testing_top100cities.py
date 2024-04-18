import pandas as pd


df = pd.read_csv("top100cities.csv", index_col=0)
df["city"] = df["city"].str.lower()
df["state"] = df["state"].str.lower()


city = input("Please enter your city:").lower()


row_for_city = df[df["city"] == city]

population = row_for_city["population_2020"]

val = df["city"] == city

i = 1

while (i <= 100):
    if(val[i] == True):
        print(val[i])
    i = i + 1




# if(df.isin([city]).any().any()):

#     print("Your city is in the top 100 most populous cities in the United States.")
#     print("According to the 2020 census " + city + " has " + str(population[1]) + " people")









