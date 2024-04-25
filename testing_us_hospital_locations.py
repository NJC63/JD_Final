import pandas as pd

df = pd.read_csv("us_hospital_locations.csv")

df["NAME"] = df["NAME"].str.lower()
df["ADDRESS"] = df["ADDRESS"].str.lower()
df["CITY"] = df["CITY"].str.lower()
df["STATE"] = df["STATE"].str.lower()
df["TYPE"] = df["TYPE"].str.lower()
df["STATUS"] = df["STATUS"].str.lower()
df["COUNTY"] = df["COUNTY"].str.lower()

city = "los angeles"
st = "ca"


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



p = 0
names, addresses, zips ,telephones, types, counties, cfips, websites = [], [], [], [], [], [], [], []

while(p < len(locations)):
    if(str(((rows[p])["STATUS"])[locations[p]]) == "open"):
        names.append(str(((rows[p])["NAME"])[locations[p]]))
        addresses.append(str(((rows[p])["ADDRESS"])[locations[p]]))
        zips.append(str(((rows[p])["ZIP"])[locations[p]]))
        telephones.append(str(((rows[p])["TELEPHONE"])[locations[p]]))
        types.append(str(((rows[p])["TYPE"])[locations[p]]))
        counties.append(str(((rows[p])["COUNTY"])[locations[p]]))
        cfips.append(str(((rows[p])["COUNTYFIPS"])[locations[p]]))
        websites.append(str(((rows[p])["WEBSITE"])[locations[p]]))
    p += 1

        

print(f"In {city.title()} there are {len(names)} open hospitals.")

print(telephones)

q = 0
while(q < len(names)):
    print(f"{names[q].title()} is located at {addresses[q].title()} {city.title()} {st.upper()} {zips[q]}.")

    if(telephones[q] != 'NOT AVAILABLE'):
        print(f"Telephone number: {telephones[q]}")
    if(websites[q] != 'NOT AVAILABLE'):
        print(f"Website: {websites[q]}")

    q += 1
    





