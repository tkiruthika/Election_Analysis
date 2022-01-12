#print("Hello World")
# counties = ["Arapahoe","Denver","Jefferson"]
'''if counties[1] == 'Denver':
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else :
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters')'''
'''voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
    for value in county_dict.values():
        print(value)'''
'''counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, value in counties_dict.items():
    print(f'{county} county has {value:,} registered voters')'''
from typing import ValuesView


voting_data = [ {"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
'''for counties_dict in voting_data:
    for i in counties_dict.values("county") and j in counties_dict.values("registered_voters"):
        print(f" {i} county has {j:,} registered voters")'''
for vd in voting_data:
    print(f'{vd["county"]} county has {vd["registered_voters"]:,} registered voters')