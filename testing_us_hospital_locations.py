import pandas as pd

df = pd.read_csv("us_hospital_locations.csv")

df["NAME"] = df["NAME"].str.lower()
df["ADDRESS"] = df["ADDRESS"].str.lower()
df["CITY"] = df["CITY"].str.lower()
df["STATE"] = df["STATE"].str.lower()
df["TYPE"] = df["TYPE"].str.lower()
df["STATUS"] = df["STATUS"].str.lower()
df["COUNTY"] = df["COUNTY"].str.lower()
df["WEBSITE"] = df["WEBSITE"].str.lower()

city = "hot springs"
st = "ar"


val = df["CITY"] == city
valSt = df["STATE"] == st
inHospitals = False
locations = []
i = 0

while (i < 7596):
    if((val[i] == True) & (valSt[i] == True)):
        inHospitals = True
        locations.append(i)
    i += 1

if(inHospitals == False):
    exit()

print(locations)
rows = []

j = 0
while (j < len(locations)):
    rows.append(df.iloc[[locations[j]]])
    j += 1


print(rows)


# name = str((row["NAME"])[location])
# address = str((row["ADDRESS"])[location])
# city = str((row["CITY"])[location])
# state = str((row["STATE"])[location])
# zip = str((row["ZIP"])[location])
# telephone = str((row["TELEPHONE"])[location])
# type = str((row["TYPE"])[location])
# status = str((row["STATUS"])[location])
# county = str((row["COUNTY"])[location])
# cfips = str((row["COUNTYFIPS"])[location])
# website = str((row["WEBSITE"])[location])




