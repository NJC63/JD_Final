import functions

import pandas as pd


# # testing the sorted() function
# list = ["a", "c", "z", "p", "d", "b", "o", "i", "q", "t", "g", "s", "r", "u", "j", "k", "v", "e", "f", "w", "x", "n", "y", "l", "h", "m"]
# sorted_list = sorted(list)
# print(sorted_list)


# # testing floor division
# print(10 // 2)
# print(10 // 3)
# print(10 // 4)


# # testing array equality
# array = [1, 2, 3, 4]
# x = 3

# print(x == array[0])


# # testing binary_search for strings
# print(binary_search.binarySearch_strings(array, 1))


# testing binsearch
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# words = ["a", "b", "c", "d", "e"]

# print(functions.binSearch(nums, 0))

# print(functions.binSearch(words, "d"))



# testing working with csv files


# Making all of the string columns lowercase
df = pd.read_csv("cities.csv", header=0)
df["city"] = df["city"].str.lower()
df["st"] = df["st"].str.lower()
df["state"] = df["state"].str.lower()
df["county"] = df["county"].str.lower()

print(df.head(10))

# Convert the column names into a list
column_names = df.columns.values.tolist()

# print(column_names)
# print(column_names[0])

pittRow = df[df[column_names[0]] == "pittsburgh"]

lat = pittRow["lat"]

'''
print(pittRow)
print(lat)


city = "Abbeville"
formatted_city = city.lower()
row = df[(df["state"] == "alabama") & (df["city"] == formatted_city)]
zip = row["zip"]

print(zip)

'''


# splitting using the ','
'''
city = "alabaster"
formatted_city = city.lower()
row = df[(df["state"] == "alabama") & (df["city"] == formatted_city)]
zip = row["zip"]

cleaned_zip = zip.str.split(",").tolist()

print(zip)
print(cleaned_zip[0][0])

'''


city = "Pittsburgh"
state = "Pennsylvania"
formatted_city = city.lower()
formatted_state = state.lower()
row = df[(df["state"] == formatted_state) & (df["city"] == formatted_city)]
zip = row["zip"]

cleaned_zip = zip.str.split("-").tolist()

print(zip)
print(cleaned_zip[0][0])







# testing .lower() function
'''
string = "DOG Dog dOg"
print(string.lower())
'''


