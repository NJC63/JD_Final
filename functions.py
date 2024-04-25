# Pandas is used for general data management
import pandas as pd

# requests_html is used for webscraping weather data from the internet
from requests_html import HTMLSession


# cities
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
        return 0, 0, 0, 0, 0

    row = df.iloc[[location]]

    st = str((row["st"])[location])
    state = str((row["state"])[location])
    county = str((row["county"])[location])
    zip = str((row["zip"])[location])
    
    # print("County for " + city.title() + " is " + county.title() + " County .")
    # print("Zip for " + city.title() + " is " + zip + ".")
        

    return st, state, county, zip, location



# top100cities
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
        return 0, 0, 0, 0


    row = df.iloc[[location]]

    state = str((row["state"])[location])
    population = str((row["population_2020"])[location])
    largestCityInState = str((row["largest_city_in_state"])[location])
    stateCapital = str((row["state_capital"])[location])
    federalCapital = str((row["federal_capital"])[location])

    return population, largestCityInState, stateCapital, federalCapital, location

# airports
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
        return 0, 0

    row = df.iloc[[location]]

    airport = str((row["AIRPORT"])[location])
    iata = str((row["IATA"])[location])

    return airport, iata

# weather
def weather(city, st):

    session = HTMLSession()

    url = f'https://www.google.com/search?q=weather+{city}+{st}'

    r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

    currentTemp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    currentCondition = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

    precipitation = r.html.find('div.wtsRwe', first=True).find('span#wob_pp', first=True).text
    humidity = r.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text
    wind = r.html.find('div.wtsRwe', first=True).find('span#wob_ws', first=True).text


    forecast = r.html.find('div.wob_dfc', first=True).find('div.wob_df')
    daysOfWeek, highTemps, lowTemps, conditions = [], [], [], []

    i = 0
    while(i < len(forecast)):
        day = forecast[i].find('div.Z1VzSb', first=True)
        daysOfWeek.append(day.text)

        high = forecast[i].find('div.gNCp2e span.wob_t', first=True)
        highTemps.append(high.text)

        low = forecast[i].find('div.QrNVmd.ZXCv8e span.wob_t', first=True)
        lowTemps.append(low.text)

        condition = forecast[i].find('img.YQ4gaf.zr758c', first=True)
        conditions.append(condition.attrs['alt'])

        i += 1


    return currentTemp, unit, currentCondition, precipitation, humidity, wind, daysOfWeek, highTemps, lowTemps, conditions




# us_hospitals
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
        return 0, 0, 0, 0, 0, 0, 0, 0

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
    
    return names, addresses, zips, telephones, types, counties, cfips, websites



def txtOutput(output, strings):
    for i in strings:
        output.write(i)
        output.write("\n")


