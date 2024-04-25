import pandas as pd

import functions as fn

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

line1 = (inputFile.readline()).strip()
line2 = (inputFile.readline()).strip()
city = ((line1[5:]).strip()).lower()
state = ((line2[6:]).strip()).lower()

st, state, county, zip, location = fn.cities(city, state)

if(st == 0):
    city = input("Please enter your desired city within the United States (city): ").lower()
    tempState = input("State (Either abbreviation or full name): ").lower()
    st, state, county, zip, location = fn.cities(city, tempState)
    if(st == 0):
        print("This location does not appear to be in the US database.")
        exit()


print()
fn.top100cities(city, state)
fn.airports(city, st)
fn.weather(city, st)
fn.us_hospitals(city, st)


strings = ["Hello\n", 
           "Test1", "Test2"]

fn.txtOutput(outputFile, strings)


inputFile.close()
outputFile.close()


