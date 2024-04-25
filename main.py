import pandas as pd

import functions as fn



city = input("Please enter your desired city within the United States (city): ").lower()
tempState = input("State (Either abbreviation or full name): ").lower()


print()

st, state, county, zip, location = fn.cities(city, tempState)
print()
fn.top100cities(city, state)
fn.airports(city, st)
fn.weather(city, st)
fn.us_hospitals(city, st)




''' 

zip code
longitude and latitude
county name
city
state

'''
