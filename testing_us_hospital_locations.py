import pandas as pd

df = pd.read_csv("us_hospital_locations.csv")

df["NAME"] = df["NAME"].str.lower()
df["ADDRESS"] = df["ADDRESS"].str.lower()
df["CITY"] = df["CITY"].str.lower()
df["STATE"] = df["STATE"].str.lower()
df["TYPE"] = df["TYPE"].str.lower()
df["STATUS"] = df["STATUS"].str.lower()
df["COUNTY"] = df["COUNTY"].str.lower()

city = input("City: ")
row_for_city = df[df["city"] == city]

val = df["city"] == city
inHospitals = False
location = -1
i = 1

while (i <= 7597):
    if(val[i] == True):
        inHospitals = True
        location = i
    i += 1

if(inHospitals):

    name_index = row_for_city["NAME"]
    address_index = row_for_city["ADDRESS"]
    city_index = row_for_city["CITY"]
    state_index = row_for_city["STATE"]
    zip_index = row_for_city["ZIP"]
    telephone_index = row_for_city["TELEPHONE"]
    type_index = row_for_city["TYPE"]
    status_index = row_for_city["STATUS"]
    county_index = row_for_city["COUNTY"]
    cfips_index = row_for_city["COUNTYFIPS"]
    website_index = row_for_city["WEBSITE"]



    name = str(name_index[location])
    address = str(address_index[location])
    city = str(city_index[location])
    state = str(state_index[location])
    zip = str(zip_index[location])
    telephone = str(telephone_index[location])
    type = str(type_index[location])
    status = str(status_index[location])
    county = str(county_index[location])
    cfips = str(cfips_index[location])
    website = str(website_index[location])

    







