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
        print("Your city and state do not appear to be in the US database.")
        exit()

    row = df.iloc[[location]]

    st = str((row["st"])[location])
    state = str((row["state"])[location])
    county = str((row["county"])[location])
    zip = str((row["zip"])[location])
    

    print(city.title() + " is in the state " + state.title() + " with initials " + st.upper() + ".")
    print("County for " + city.title() + " is " + county.title() + " County .")
    print("Zip for " + city.title() + " is " + zip + ".")
        

    return st, state, county, zip, location




def top100cities(city):

    df = pd.read_csv("top100cities.csv", index_col=0)
    df["city"] = df["city"].str.lower()
    df["state"] = df["state"].str.lower()

    row_for_city = df[df["city"] == city]
    state = row_for_city["state"]
    population = row_for_city["population_2020"]
    largestCityInState = row_for_city["largest_city_in_state"]
    stateCapital = row_for_city["state_capital"]
    federalCapital = row_for_city["federal_capital"]


    # Checking for if the value is in the top 100 most populous cities
    val = df["city"] == city

    inTop100 = False
    location = -1
    i = 1
    while (i <= 100):
        if(val[i] == True):
            inTop100 = True
            location = i
        i = i + 1
    
    if(inTop100):

        city = city.title()

        print("Your city is in the top 100 most populous cities within the United States.")
        print("According to the 2020 census " + city + " has " + str(population[location]) + " people.")

        print(city + " is ranked as the number " + str(location) + " most populous city within the U.S.")

        if(largestCityInState[location] == True): print(city + " is the largest city within " + state[location].title() + ".")
        if(stateCapital[location] == True): print(city + " is the state capital in " + state[location].title() + ".")
        if(federalCapital[location] == True): print(city + " is the federal capital.")



def airports(city):
    df = pd.read_csv("airports.csv")

    df["CITY"] = df["CITY"].str.lower()
    df["STATE"] = df["STATE"].str.lower()

    row_for_city = df[df["CITY"] == city]

    airport = row_for_city["AIRPORT"]
    iata = row_for_city["IATA"]

    val = df["CITY"] == city
    inAirports = False
    location = -1
    i = 1
    while (i <= 340):
        if(val[i] == True):
            inAirports = True
            location = i
        i = i + 1

    if(inAirports):
        print("The main airport for " + city.title() + " is " + str(airport[location]) + " Airport.")
        print("The IATA code for " + str(airport[location]) + " is " + str(iata[location]) + ".")


def weather(city, st):

    session = HTMLSession()

    url = f'https://www.google.com/search?q=weather+{city}+{st}'

    r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

    temperature = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    condition = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

    print(f"The current weather conditions in {city.title()} are {temperature} {unit} and {condition}.")


















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