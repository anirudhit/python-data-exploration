import json
import pprint
with open("data/json/sample-weather-history.json","r") as weatherfile:
    weatherdata = json.load(weatherfile)

# if file loaded
print(len(weatherdata))

# load the first entry
pprint.pp(weatherdata[0])

# entries on each year
years = {}
for d in weatherdata:
    key = d['date'][0:4]
    if(key in years):
        years[key]+= 1
    else:
        years[key]= 1

pprint.pp(years, width=5)