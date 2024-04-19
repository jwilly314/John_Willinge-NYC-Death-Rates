import json
import csv

dictionary = {}

with open("nycMortality_borough.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Borough"] not in dictionary: dictionary[row["Borough"]] = []
        dictionary[row["Borough"]].append(row["2007"])
        dictionary[row["Borough"]].append(row["2008"])
        dictionary[row["Borough"]].append(row["2009"])
        dictionary[row["Borough"]].append(row["2010"])
        dictionary[row["Borough"]].append(row["2011"])
        dictionary[row["Borough"]].append(row["2012"])
        dictionary[row["Borough"]].append(row["2013"])
        dictionary[row["Borough"]].append(row["2014"])
        dictionary[row["Borough"]].append(row["2015"])
        dictionary[row["Borough"]].append(row["2016"])
        
print(dictionary)

#Save the json object to a file
f2 = open("nycMortality_borough.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()