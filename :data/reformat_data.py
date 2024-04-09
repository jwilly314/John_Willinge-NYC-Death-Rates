import json


f1 = open("nycMortality_area.csv", "r")
lines = f1.readlines()

dictionary = {}



f1.close()

#Save the json object to a file
f2 = open("nycMortality_area.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()