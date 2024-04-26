# Pandas is used for general data management
import pandas as pd

# requests_html is used for webscraping weather data from the internet
from requests_html import HTMLSession


# cities
def cities(city, state):

    # Creating a pandas dataframe for cities.csv
    df = pd.read_csv("cities.csv")

    # Making each column lowercase for easier searching
    df["city"] = df["city"].str.lower()
    df["st"] = df["st"].str.lower()
    df["state"] = df["state"].str.lower()


    val = df["city"] == city

    inCities = False
    location = -1
    i = 1

    # Searching for city and state with state initials
    if(len(state) == 2):
        valSt = df["st"] == state
        while (i <= 19501):
            if((val[i] == True) & (valSt[i] == True)):
                inCities = True
                location = i
            i += 1

    # Searching for city and state with full state name
    else:
        valState = df["state"] == state
        while (i <= 19501):
            if((val[i] == True) & (valState[i] == True)):
                inCities = True
                location = i
            i += 1

    # Case for if the city and state are not found within the database
    if(inCities == False):
        return 0, 0, 0, 0, 0

    row = df.iloc[[location]]

    # Assigning the state initials, state name, county and zip codes to variables
    st = str((row["st"])[location])
    state = str((row["state"])[location])
    county = str((row["county"])[location])
    zip = str((row["zip"])[location])
        
    return st, state, county, zip, location



# top100cities
def top100cities(city, state):

    # Reading in the top100cities.csv into a pandas dataframe and then making columns lowercase
    df = pd.read_csv("top100cities.csv")
    df["city"] = df["city"].str.lower()
    df["state"] = df["state"].str.lower()

    # Checking for if the value is in the top 100 most populous cities
    inTop100 = False
    location = -1
    i = 0

    # Searching for city and state in top100cities.csv
    val = df["city"] == city
    valState = df["state"] == state
    while (i < 100):
        if((val[i] == True) & (valState[i] == True)):
            inTop100 = True
            location = i
        i += 1

    # Case for not in the top 100 database
    if(inTop100 == False):
        return 0, 0, 0, 0, 0


    row = df.iloc[[location]]

    # Variables for appropriate data gathered
    state = str((row["state"])[location])
    population = str((row["population_2020"])[location])
    largestCityInState = str((row["largest_city_in_state"])[location])
    stateCapital = str((row["state_capital"])[location])
    federalCapital = str((row["federal_capital"])[location])

    return population, largestCityInState, stateCapital, federalCapital, location

# airports
def airports(city, st):

    # Reading in airports.csv with pandas
    df = pd.read_csv("airports.csv")
    
    # Formatting each column to be lowercase
    df["CITY"] = df["CITY"].str.lower()
    df["STATE"] = df["STATE"].str.lower()
    df["COUNTRY"] = df["COUNTRY"].str.lower()

    inAirports = False
    location = -1
    i = 1

    # Searching for city and state in the airports.csv
    val = df["CITY"] == city
    valSt = df["STATE"] == st
    while (i <= 340):
        if((val[i] == True) & (valSt[i] == True)):
            inAirports = True
            location = i
        i += 1

    # Case for if the city and state are not in the database
    if(inAirports == False):
        return 0, 0

    row = df.iloc[[location]]

    airport = str((row["AIRPORT"])[location])
    iata = str((row["IATA"])[location])

    return airport, iata

# weather
def weather(city, st):

    # Creating a HTML session
    session = HTMLSession()

    # Creating the f-string url
    url = f'https://www.google.com/search?q=weather+{city}+{st}'

    # Allowing the html session to access the internet through my user-agent
    r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

    # Initial data that was scraped using the video tutorial
    currentTemp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    currentCondition = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

    # Data scraped using my own techniques
    precipitation = r.html.find('div.wtsRwe', first=True).find('span#wob_pp', first=True).text
    humidity = r.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text
    wind = r.html.find('div.wtsRwe', first=True).find('span#wob_ws', first=True).text

    # Scraping the data for the next 8 days
    forecast = r.html.find('div.wob_dfc', first=True).find('div.wob_df')
    daysOfWeek, highTemps, lowTemps, conditions = [], [], [], []

    # Searching the list of forecast for the specific actions that I want and adding them to lists
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

    # Reading in the us_hospital_locations.csv using pandas
    df = pd.read_csv("us_hospital_locations.csv")

    # Formatting the columns to lowercase
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

    # Searching for the city and state within the hospitals database
    i = 0
    while (i < 7596):
        if((val[i] == True) & (valSt[i] == True)):
            inHospitals = True
            locations.append(i)
        i += 1

    # Case for if the city and state are not found within the database
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


# txtOutput writes the strings array to the appropriate output file
def txtOutput(output, strings):
    for i in strings:
        output.write(i)
        output.write("\n")


