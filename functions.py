import pandas as pd
from requests_html import HTMLSession


def cities(city, state):
    df = pd.read_csv("cities.csv")

    df["city"] = df["city"].str.lower()
    df["st"] = df["st"].str.lower()
    df["state"] = df["state"].str.lower()


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
        print("This location does not appear to be in the US database.")
        exit()

    row = df.iloc[[location]]

    st = str((row["st"])[location])
    state = str((row["state"])[location])
    county = str((row["county"])[location])
    zip = str((row["zip"])[location])
    

    print(city.title() + " is in the state " + state.title() + " with initials " + st.upper() + ".")
    # print("County for " + city.title() + " is " + county.title() + " County .")
    # print("Zip for " + city.title() + " is " + zip + ".")
        

    return st, state, county, zip, location




def top100cities(city, state):

    df = pd.read_csv("top100cities.csv")
    df["city"] = df["city"].str.lower()
    df["state"] = df["state"].str.lower()

    # Checking for if the value is in the top 100 most populous cities
    inTop100 = False
    location = -1
    i = 0

    val = df["city"] == city
    valState = df["state"] == state
    while (i < 100):
        if((val[i] == True) & (valState[i] == True)):
            inTop100 = True
            location = i
        i += 1

    if(inTop100 == False):
        return


    row = df.iloc[[location]]

    state = str((row["state"])[location])
    population = str((row["population_2020"])[location])
    largestCityInState = str((row["largest_city_in_state"])[location])
    stateCapital = str((row["state_capital"])[location])
    federalCapital = str((row["federal_capital"])[location])

    city = city.title()

    print("Your city is in the top 100 most populous cities within the United States.")
    print("According to the 2020 census " + city + " has " + population + " people.")

    print(city + " is ranked as the number " + str(location + 1) + " most populous city within the U.S.")

    if(largestCityInState == True): print(city + " is the largest city within " + state.title() + ".")
    if(stateCapital == True): print(city + " is the state capital in " + state.title() + ".")
    if(federalCapital == True): print(city + " is the federal capital.")

    print()


def airports(city, st):
    df = pd.read_csv("airports.csv")

    df["CITY"] = df["CITY"].str.lower()
    df["STATE"] = df["STATE"].str.lower()
    df["COUNTRY"] = df["COUNTRY"].str.lower()

    inAirports = False
    location = -1
    i = 1

    val = df["CITY"] == city
    valSt = df["STATE"] == st
    while (i <= 340):
        if((val[i] == True) & (valSt[i] == True)):
            inAirports = True
            location = i
        i += 1

    if(inAirports == False):
        return

    row = df.iloc[[location]]

    airport = str((row["AIRPORT"])[location])
    iata = str((row["IATA"])[location])

    print("The main airport for " + city.title() + " is " + airport + " Airport.")
    print("The IATA code for " + airport + " is " + iata + ".")
    print()


def weather(city, st):

    session = HTMLSession()

    url = f'https://www.google.com/search?q=weather+{city}+{st}'

    r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

    temperature = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    condition = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

    print(f"The current weather conditions in {city.title()} are {temperature} {unit} and {condition}.")
    print()





def us_hospitals(city, st):
    df = pd.read_csv("us_hospital_locations.csv")

    df["NAME"] = df["NAME"].str.lower()
    df["ADDRESS"] = df["ADDRESS"].str.lower()
    df["CITY"] = df["CITY"].str.lower()
    df["STATE"] = df["STATE"].str.lower()
    df["TYPE"] = df["TYPE"].str.lower()
    df["STATUS"] = df["STATUS"].str.lower()
    df["COUNTY"] = df["COUNTY"].str.lower()


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
        return

    rows = []

    j = 0
    while (j < len(locations)):
        rows.append(df.iloc[[locations[j]]])
        j += 1

    
    names, addresses, zips ,telephones, types, counties, cfips, websites = [], [], [], [], [], [], [], []

    p = 0
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

    q = 0
    while(q < len(names)):
        print(f"{names[q].title()} is located at {addresses[q].title()} {city.title()} {st.upper()} {zips[q]}.")

        if(telephones[q] != 'NOT AVAILABLE'):
            print(f"Telephone number: {telephones[q]}")
        if(websites[q] != 'NOT AVAILABLE'):
            print(f"Website: {websites[q]}")

        q += 1
    print()












# ------------------ Potentially useful ------------------ #



# attempt to split the zips and organize correctly
def zipsInOrder(zip):
    zip = str(zip)
    original_list = zip.rsplit("-")
    print(original_list)
    initial = original_list[0][0]
    final = original_list[0][1]

    count = initial
    i = 1
    final_list = [initial, final]
    while(count < final):
        count = str(int(count) + 1)
        final_list.insert(i, count)
        return final_list
    return zip
    

def binarySearch(sorted_list, target):
    min = 0
    max = len(sorted_list) - 1

    while(min <= max):
        midpt = (min + max)//2

        if(sorted_list[midpt] == target):
            return midpt
        elif(sorted_list[midpt] > target):
            max = midpt - 1
        elif(sorted_list[midpt] < target):
            min = midpt + 1
    return -1   

def clean(raw_df):

    column_names = raw_df.columns.values.tolist()


    return 1