import json
import pprint
with open("data/json/sample-weather-history.json","r") as weatherfile:
    weatherdata = json.load(weatherfile)

# warmest day in the entire dataset
warmday = max(weatherdata, key = lambda x: x['tmax'])
print(f"The warment day is {warmday['date']} with {warmday['tmax']} degrees")
    
# coldest day in the entire dataset
coldday = min(weatherdata, key = lambda x: x['tmin'])
print(f"The coldest day is {coldday['date']} with {coldday['tmin']} degrees")
    
# Total days with snow fall
snowdays = [day for day in weatherdata if day['snow'] > 0]
print(f"Snow fell on {len(snowdays)} days")
pprint.pp(snowdays)