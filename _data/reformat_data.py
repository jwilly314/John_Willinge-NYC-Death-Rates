import json
import csv

dictionary = {}

with open("nycMortality_area.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Geography"] not in dictionary: dictionary[row["Geography"]] = []
        dictionary[row["Geography"]].append(row["Age-adjusted rate per 1000"])


print(dictionary)

#Save the json object to a file
f2 = open("nycMortality_area.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()