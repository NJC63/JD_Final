import pandas as pd

import functions as fn

# Opening input and output files
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

# Reading in the city and state provided in input.txt and cleaning up the values
line1 = (inputFile.readline()).strip()
line2 = (inputFile.readline()).strip()
city = ((line1[5:]).strip()).lower()
state = ((line2[6:]).strip()).lower()

st, state, county, zip, location = fn.cities(city, state)


# If the city and state is at a valid location then continue otherwise prompt user input
if(st == 0):
    city = input("Please enter your desired city within the United States (city): ").lower()
    tempState = input("State (Either abbreviation or full name): ").lower()
    st, state, county, zip, location = fn.cities(city, tempState)
    if(st == 0):
        print("This location does not appear to be in the US database.")
        exit()

# Calling the functions to get appropriate data from the databases and online weather
print()
population, largestCityInState, stateCapital, federalCapital, rank = fn.top100cities(city, state)
airport, iata = fn.airports(city, st)
currentTemp, unit, currentCondition, precipitation, humidity, wind, daysOfWeek, highTemps, lowTemps, conditions = fn.weather(city, st)
names, addresses, zips, telephones, types, counties, cfips, websites = fn.us_hospitals(city, st)


strings = []

strings.append("BASIC INFO:\n")
strings.append(f"{city.title()} is in the state {state.title()} with initials {st.upper()}")


if(population != 0):
    strings.append("\n\nPOPULARITY:\n")
    strings.append("Your city is in the top 100 most populous cities within the United States.")
    strings.append("According to the 2020 census " + city.title() + " has " + population + " people.")
    strings.append(city.title() + " is ranked as the number " + str(rank + 1) + " most populous city within the U.S.\n")

    if(largestCityInState == True): strings.append(city + " is the largest city within " + state.title() + ".")
    if(stateCapital == True): strings.append(city + " is the state capital in " + state.title() + ".")
    if(federalCapital == True): strings.append(city + " is the federal capital.")

if(airport != 0):
    strings.append("\n\nAIRPORT:\n")
    strings.append("The main airport for " + city.title() + " is " + airport + " Airport.")
    strings.append("The IATA code for " + airport + " is " + iata + ".\n")

strings.append("\n\nWEATHER:")
strings.append(f"\nCurrent weather conditions in {city.title()} {st.upper()} are:\n{currentTemp} {unit} and {currentCondition} \nPrecipitation: {precipitation} \nHumidity: {humidity} \nWind: {wind}\n")
strings.append(f"The forecast for the next 8 days is:\n")
i = 0
while(i < len(daysOfWeek)):
    strings.append(f"   {daysOfWeek[i]}   {highTemps[i]}/{lowTemps[i]} {unit}    {str(conditions[i]).title()}")
    i += 1


if(names != 0):
    strings.append("\n\nHOSPITALS:\n")
    strings.append(f"In {city.title()} there are {len(names)} open hospitals.\n")

    q = 0
    while(q < len(names)):
        strings.append(f"{names[q].title()} is located at {addresses[q].title()} {city.title()} {st.upper()} {zips[q]}.")

        if(telephones[q] != 'NOT AVAILABLE'):
            strings.append(f"   Telephone number: {telephones[q]}")
        if(websites[q] != 'NOT AVAILABLE'):
            strings.append(f"   Website: {websites[q]}\n")

        q += 1



# Printing to the terminal
j = 0
while(j < len(strings)):
    print(strings[j])
    j += 1

# Printing to the output file
fn.txtOutput(outputFile, strings)

# Closing files
inputFile.close()
outputFile.close()


