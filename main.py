import pandas as pd

import functions as fn



city = input("Please enter your desired city within the United States (city): ").lower()
print()

st, state, county, zip = fn.cities(city)
print()
fn.top100cities(city)
print()
fn.airports(city)
print()
fn.weather(city, st)




''' 

zip code
longitude and latitude
county name
city
state

'''
