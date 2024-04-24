import pandas as pd

import functions as fn



city = input("Please enter your desired city within the United States (city): ").lower()
state = input("State (Either abbreviation or full name): ").lower()


print()

st, state, county, zip, location = fn.cities(city, state)
print()
fn.top100cities(city)
print()
fn.airports(city)
print()
fn.weather(city, st)
print()




''' 

zip code
longitude and latitude
county name
city
state

'''
