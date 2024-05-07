from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/about')
def about2():
    return render_template('about.html')

@app.route('/nyc')
def macro():
    f = open("_data/nycMortality_area.json", "r")
    data = json.load(f)
    f.close()

    neighborhoods = list(data.keys())

    fills = []

    for neighborhood in neighborhoods:
        if 0 <= float(data[neighborhood][0]) < 1:
            fills.append("#ffcccc")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#ff9999")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#ff6666")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#ff3333")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#ff0000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#cc0000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#990000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#660000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#330000")
        elif 3 <= float(data[neighborhood][0]) <= 10:
            fills.append("#190000")

    return render_template('macro.html', name="NYC", data=data, fills=fills)

@app.route('/manhattan')
def micro1():
    f = open("_data/nycMortality_area.json", "r")
    data = json.load(f)
    f.close()

    g = open("_data/nycMortality_borough.json", "r")
    data2 = json.load(g)
    g.close()

    boroughs = list(data2.keys())
    averageData = 0
    averageChange = 0

    for borough in boroughs:
        averageChange += (float(data2[borough][0])-float(data2[borough][9]))
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50
    averageChange = averageChange/5

    points = ""

    year = 2007
    for value in data2[boroughs[0]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    boroughChange = float(data2[boroughs[0]][0])-float(data2[boroughs[0]][9])
    points = points[:-1]

    neighborhoods = list(data.keys())

    fills = []

    highest = 0
    highest2 = 0
    lowest = 100
    lowest2 = 100

    highestNeighborhood = ''
    highestNeighborhood2 = ''
    lowestNeighborhood = ''
    lowestNeighborhood2 = ''

    averageData2 = 0
    boroughAverage = 0
    count = 0

    for neighborhood in neighborhoods:
        averageData2 += float(data[neighborhood][0])

        if data[neighborhood][1] != "3":
            fills.append("lightgray")
        else:
            boroughAverage += float(data[neighborhood][0])
            count += 1
            if 0 <= float(data[neighborhood][0]) < 1:
                fills.append("#ffcccc")
            elif 1 <= float(data[neighborhood][0]) < 1.25:
                fills.append("#ff9999")
            elif 1.25 <= float(data[neighborhood][0]) < 1.5:
                fills.append("#ff6666")
            elif 1.5 <= float(data[neighborhood][0]) < 1.75:
                fills.append("#ff3333")
            elif 1.75 <= float(data[neighborhood][0]) < 2:
                fills.append("#ff0000")
            elif 2 <= float(data[neighborhood][0]) < 2.25:
                fills.append("#cc0000")
            elif 2.25 <= float(data[neighborhood][0]) < 2.5:
                fills.append("#990000")
            elif 2.5 <= float(data[neighborhood][0]) < 2.75:
                fills.append("#660000")
            elif 2.75 <= float(data[neighborhood][0]) < 3:
                fills.append("#330000")
            elif 3 <= float(data[neighborhood][0]) <= 10:
                fills.append("#190000")

            if float(data[neighborhood][0]) > float(highest):
                highestNeighborhood2 = highestNeighborhood
                highestNeighborhood = neighborhood
                highest2 = highest
                highest = data[neighborhood][0]
            elif float(data[neighborhood][0]) > float(highest2):
                highestNeighborhood2 = neighborhood
                highest2 = data[neighborhood][0]

            if float(data[neighborhood][0]) < float(lowest):
                lowestNeighborhood2 = lowestNeighborhood
                lowestNeighborhood = neighborhood
                lowest2 = lowest
                lowest = data[neighborhood][0]
            elif float(data[neighborhood][0]) < float(lowest2):
                lowestNeighborhood2 = neighborhood
                lowest2 = data[neighborhood][0]
    
    averageData2 = averageData2/42
    boroughAverage = boroughAverage/count

    if float(boroughAverage) > float(averageData2+1):
        descriptor1 = "significantly higher than"
    elif float(boroughAverage) > float(averageData2+0.75):
        descriptor1 = "notably higher than"
    elif float(boroughAverage) > float(averageData2+0.5):
        descriptor1 = "moderately higher than"
    elif float(boroughAverage) > float(averageData2+0.25):
        descriptor1 = "slightly higher than"
    elif float(boroughAverage) > float(averageData2):
        descriptor1 = "close to"
    elif float(boroughAverage) > float(averageData2-0.25):
        descriptor1 = "slightly lower than"
    elif float(boroughAverage) > float(averageData2-0.5):
        descriptor1 = "moderately lower than"
    elif float(boroughAverage) > float(averageData2-0.75):
        descriptor1 = "notably lower than"
    else:
        descriptor1 = "significantly lower than"

    if float(data[highestNeighborhood][0]) > float(averageData2+1):
        descriptor2 = "significantly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.75):
        descriptor2 = "notably higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.5):
        descriptor2 = "moderately higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.25):
        descriptor2 = "slightly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2):
        descriptor2 = "close to"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.25):
        descriptor2 = "slightly lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.5):
        descriptor2 = "moderately lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.75):
        descriptor2 = "notably lower than"
    else:
        descriptor2 = "significantly lower than"

    if float(data[highestNeighborhood2][0]) > float(averageData2+1):
        descriptor3 = "significantly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor3 = "notably higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor3 = "moderately higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor3 = "slightly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2):
        descriptor3 = "close to"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor3 = "slightly lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor3 = "moderately lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor3 = "notably lower than"
    else:
        descriptor3 = "significantly lower than"

    if float(data[lowestNeighborhood][0]) > float(averageData2+1):
        descriptor4 = "significantly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.75):
        descriptor4 = "notably higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.5):
        descriptor4 = "moderately higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.25):
        descriptor4 = "slightly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2):
        descriptor4 = "close to"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.25):
        descriptor4 = "slightly lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.5):
        descriptor4 = "moderately lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.75):
        descriptor4 = "notably lower than"
    else:
        descriptor4 = "significantly lower than"

    if float(data[lowestNeighborhood2][0]) > float(averageData2+1):
        descriptor5 = "significantly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor5 = "notably higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor5 = "moderately higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor5 = "slightly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2):
        descriptor5 = "close to"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor5 = "slightly lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor5 = "moderately lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor5 = "notably lower than"
    else:
        descriptor5 = "significantly lower than"

    if float(boroughChange) > float(averageChange+0.4):
        descriptor6 = "significantly higher than"
        descriptor7 = "significantly high"
    elif float(boroughChange) > float(averageChange+0.3):
        descriptor6 = "notably higher than"
        descriptor7 = "notably high"
    elif float(boroughChange) > float(averageChange+0.2):
        descriptor6 = "moderately higher than"
        descriptor7 = "moderately high"
    elif float(boroughChange) > float(averageChange+0.1):
        descriptor6 = "slightly higher than"
        descriptor7 = "slightly high"
    elif float(boroughChange) > float(averageChange):
        descriptor6 = "close to"
        descriptor7 = "comparable"
    elif float(boroughChange) > float(averageChange-0.1):
        descriptor6 = "slightly lower than"
        descriptor7 = "slightly underwhelming"
    elif float(boroughChange) > float(averageChange-0.2):
        descriptor6 = "moderately lower than"
        descriptor7 = "moderately underwhelming"
    elif float(boroughChange) > float(averageChange-0.3):
        descriptor6 = "notably lower than"
        descriptor7 = "notably little"
    else:
        descriptor6 = "significantly lower than"
        descriptor7 = "significantly little"

    name=boroughs[0]

    return render_template('micro.html', aC=round(averageChange, 2), bC=round(boroughChange, 2), d6=descriptor6, d7=descriptor7, aD=round(averageData2, 1), bA=round(boroughAverage, 1), d1=descriptor1, hN=highestNeighborhood, d2=descriptor2, hN2=highestNeighborhood2, d3=descriptor3, lN=lowestNeighborhood, d4=descriptor4, lN2=lowestNeighborhood2, d5=descriptor5, name=name, fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+5.5)

@app.route('/bronx')
def micro2():

    f = open("_data/nycMortality_area.json", "r")
    data = json.load(f)
    f.close()

    g = open("_data/nycMortality_borough.json", "r")
    data2 = json.load(g)
    g.close()

    boroughs = list(data2.keys())
    averageData = 0
    averageChange = 0

    for borough in boroughs:
        averageChange += (float(data2[borough][0])-float(data2[borough][9]))
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50
    averageChange = averageChange/5

    points = ""

    year = 2007
    for value in data2[boroughs[1]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    boroughChange = float(data2[boroughs[1]][0])-float(data2[boroughs[1]][9])
    points = points[:-1]

    neighborhoods = list(data.keys())

    fills = []

    highest = 0
    highest2 = 0
    lowest = 100
    lowest2 = 100

    highestNeighborhood = ''
    highestNeighborhood2 = ''
    lowestNeighborhood = ''
    lowestNeighborhood2 = ''

    averageData2 = 0
    boroughAverage = 0
    count = 0

    for neighborhood in neighborhoods:
        averageData2 += float(data[neighborhood][0])

        if data[neighborhood][1] != "1":
            fills.append("lightgray")
        else:
            boroughAverage += float(data[neighborhood][0])
            count += 1
            if 0 <= float(data[neighborhood][0]) < 1:
                fills.append("#ffcccc")
            elif 1 <= float(data[neighborhood][0]) < 1.25:
                fills.append("#ff9999")
            elif 1.25 <= float(data[neighborhood][0]) < 1.5:
                fills.append("#ff6666")
            elif 1.5 <= float(data[neighborhood][0]) < 1.75:
                fills.append("#ff3333")
            elif 1.75 <= float(data[neighborhood][0]) < 2:
                fills.append("#ff0000")
            elif 2 <= float(data[neighborhood][0]) < 2.25:
                fills.append("#cc0000")
            elif 2.25 <= float(data[neighborhood][0]) < 2.5:
                fills.append("#990000")
            elif 2.5 <= float(data[neighborhood][0]) < 2.75:
                fills.append("#660000")
            elif 2.75 <= float(data[neighborhood][0]) < 3:
                fills.append("#330000")
            elif 3 <= float(data[neighborhood][0]) <= 10:
                fills.append("#190000")

            if float(data[neighborhood][0]) > float(highest):
                highestNeighborhood2 = highestNeighborhood
                highestNeighborhood = neighborhood
                highest2 = highest
                highest = data[neighborhood][0]
            elif float(data[neighborhood][0]) > float(highest2):
                highestNeighborhood2 = neighborhood
                highest2 = data[neighborhood][0]

            if float(data[neighborhood][0]) < float(lowest):
                lowestNeighborhood2 = lowestNeighborhood
                lowestNeighborhood = neighborhood
                lowest2 = lowest
                lowest = data[neighborhood][0]
            elif float(data[neighborhood][0]) < float(lowest2):
                lowestNeighborhood2 = neighborhood
                lowest2 = data[neighborhood][0]
    
    averageData2 = averageData2/42
    boroughAverage = boroughAverage/count

    if float(boroughAverage) > float(averageData2+1):
        descriptor1 = "significantly higher than"
    elif float(boroughAverage) > float(averageData2+0.75):
        descriptor1 = "notably higher than"
    elif float(boroughAverage) > float(averageData2+0.5):
        descriptor1 = "moderately higher than"
    elif float(boroughAverage) > float(averageData2+0.25):
        descriptor1 = "slightly higher than"
    elif float(boroughAverage) > float(averageData2):
        descriptor1 = "close to"
    elif float(boroughAverage) > float(averageData2-0.25):
        descriptor1 = "slightly lower than"
    elif float(boroughAverage) > float(averageData2-0.5):
        descriptor1 = "moderately lower than"
    elif float(boroughAverage) > float(averageData2-0.75):
        descriptor1 = "notably lower than"
    else:
        descriptor1 = "significantly lower than"

    if float(data[highestNeighborhood][0]) > float(averageData2+1):
        descriptor2 = "significantly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.75):
        descriptor2 = "notably higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.5):
        descriptor2 = "moderately higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.25):
        descriptor2 = "slightly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2):
        descriptor2 = "close to"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.25):
        descriptor2 = "slightly lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.5):
        descriptor2 = "moderately lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.75):
        descriptor2 = "notably lower than"
    else:
        descriptor2 = "significantly lower than"

    if float(data[highestNeighborhood2][0]) > float(averageData2+1):
        descriptor3 = "significantly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor3 = "notably higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor3 = "moderately higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor3 = "slightly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2):
        descriptor3 = "close to"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor3 = "slightly lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor3 = "moderately lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor3 = "notably lower than"
    else:
        descriptor3 = "significantly lower than"

    if float(data[lowestNeighborhood][0]) > float(averageData2+1):
        descriptor4 = "significantly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.75):
        descriptor4 = "notably higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.5):
        descriptor4 = "moderately higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.25):
        descriptor4 = "slightly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2):
        descriptor4 = "close to"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.25):
        descriptor4 = "slightly lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.5):
        descriptor4 = "moderately lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.75):
        descriptor4 = "notably lower than"
    else:
        descriptor4 = "significantly lower than"

    if float(data[lowestNeighborhood2][0]) > float(averageData2+1):
        descriptor5 = "significantly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor5 = "notably higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor5 = "moderately higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor5 = "slightly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2):
        descriptor5 = "close to"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor5 = "slightly lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor5 = "moderately lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor5 = "notably lower than"
    else:
        descriptor5 = "significantly lower than"

    if float(boroughChange) > float(averageChange+0.4):
        descriptor6 = "significantly higher than"
        descriptor7 = "significantly high"
    elif float(boroughChange) > float(averageChange+0.3):
        descriptor6 = "notably higher than"
        descriptor7 = "notably high"
    elif float(boroughChange) > float(averageChange+0.2):
        descriptor6 = "moderately higher than"
        descriptor7 = "moderately high"
    elif float(boroughChange) > float(averageChange+0.1):
        descriptor6 = "slightly higher than"
        descriptor7 = "slightly high"
    elif float(boroughChange) > float(averageChange):
        descriptor6 = "close to"
        descriptor7 = "comparable"
    elif float(boroughChange) > float(averageChange-0.1):
        descriptor6 = "slightly lower than"
        descriptor7 = "slightly underwhelming"
    elif float(boroughChange) > float(averageChange-0.2):
        descriptor6 = "moderately lower than"
        descriptor7 = "moderately underwhelming"
    elif float(boroughChange) > float(averageChange-0.3):
        descriptor6 = "notably lower than"
        descriptor7 = "notably little"
    else:
        descriptor6 = "significantly lower than"
        descriptor7 = "significantly little"

    name=boroughs[1]

    return render_template('micro.html', aC=round(averageChange, 2), bC=round(boroughChange, 2), d6=descriptor6, d7=descriptor7, aD=round(averageData2, 1), bA=round(boroughAverage, 1), d1=descriptor1, hN=highestNeighborhood, d2=descriptor2, hN2=highestNeighborhood2, d3=descriptor3, lN=lowestNeighborhood, d4=descriptor4, lN2=lowestNeighborhood2, d5=descriptor5, name=name, fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)-0.5)

@app.route('/brooklyn')
def micro3():
    f = open("_data/nycMortality_area.json", "r")
    data = json.load(f)
    f.close()

    g = open("_data/nycMortality_borough.json", "r")
    data2 = json.load(g)
    g.close()

    boroughs = list(data2.keys())
    averageData = 0
    averageChange = 0

    for borough in boroughs:
        averageChange += (float(data2[borough][0])-float(data2[borough][9]))
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50
    averageChange = averageChange/5

    points = ""

    year = 2007
    for value in data2[boroughs[2]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    boroughChange = float(data2[boroughs[2]][0])-float(data2[boroughs[2]][9])
    points = points[:-1]

    neighborhoods = list(data.keys())

    fills = []

    highest = 0
    highest2 = 0
    lowest = 100
    lowest2 = 100

    highestNeighborhood = ''
    highestNeighborhood2 = ''
    lowestNeighborhood = ''
    lowestNeighborhood2 = ''

    averageData2 = 0
    boroughAverage = 0
    count = 0

    for neighborhood in neighborhoods:
        averageData2 += float(data[neighborhood][0])

        if data[neighborhood][1] != "2":
            fills.append("lightgray")
        else:
            boroughAverage += float(data[neighborhood][0])
            count += 1
            if 0 <= float(data[neighborhood][0]) < 1:
                fills.append("#ffcccc")
            elif 1 <= float(data[neighborhood][0]) < 1.25:
                fills.append("#ff9999")
            elif 1.25 <= float(data[neighborhood][0]) < 1.5:
                fills.append("#ff6666")
            elif 1.5 <= float(data[neighborhood][0]) < 1.75:
                fills.append("#ff3333")
            elif 1.75 <= float(data[neighborhood][0]) < 2:
                fills.append("#ff0000")
            elif 2 <= float(data[neighborhood][0]) < 2.25:
                fills.append("#cc0000")
            elif 2.25 <= float(data[neighborhood][0]) < 2.5:
                fills.append("#990000")
            elif 2.5 <= float(data[neighborhood][0]) < 2.75:
                fills.append("#660000")
            elif 2.75 <= float(data[neighborhood][0]) < 3:
                fills.append("#330000")
            elif 3 <= float(data[neighborhood][0]) <= 10:
                fills.append("#190000")

            if float(data[neighborhood][0]) > float(highest):
                highestNeighborhood2 = highestNeighborhood
                highestNeighborhood = neighborhood
                highest2 = highest
                highest = data[neighborhood][0]
            elif float(data[neighborhood][0]) > float(highest2):
                highestNeighborhood2 = neighborhood
                highest2 = data[neighborhood][0]

            if float(data[neighborhood][0]) < float(lowest):
                lowestNeighborhood2 = lowestNeighborhood
                lowestNeighborhood = neighborhood
                lowest2 = lowest
                lowest = data[neighborhood][0]
            elif float(data[neighborhood][0]) < float(lowest2):
                lowestNeighborhood2 = neighborhood
                lowest2 = data[neighborhood][0]
    
    averageData2 = averageData2/42
    boroughAverage = boroughAverage/count

    if float(boroughAverage) > float(averageData2+1):
        descriptor1 = "significantly higher than"
    elif float(boroughAverage) > float(averageData2+0.75):
        descriptor1 = "notably higher than"
    elif float(boroughAverage) > float(averageData2+0.5):
        descriptor1 = "moderately higher than"
    elif float(boroughAverage) > float(averageData2+0.25):
        descriptor1 = "slightly higher than"
    elif float(boroughAverage) > float(averageData2):
        descriptor1 = "close to"
    elif float(boroughAverage) > float(averageData2-0.25):
        descriptor1 = "slightly lower than"
    elif float(boroughAverage) > float(averageData2-0.5):
        descriptor1 = "moderately lower than"
    elif float(boroughAverage) > float(averageData2-0.75):
        descriptor1 = "notably lower than"
    else:
        descriptor1 = "significantly lower than"

    if float(data[highestNeighborhood][0]) > float(averageData2+1):
        descriptor2 = "significantly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.75):
        descriptor2 = "notably higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.5):
        descriptor2 = "moderately higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.25):
        descriptor2 = "slightly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2):
        descriptor2 = "close to"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.25):
        descriptor2 = "slightly lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.5):
        descriptor2 = "moderately lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.75):
        descriptor2 = "notably lower than"
    else:
        descriptor2 = "significantly lower than"

    if float(data[highestNeighborhood2][0]) > float(averageData2+1):
        descriptor3 = "significantly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor3 = "notably higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor3 = "moderately higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor3 = "slightly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2):
        descriptor3 = "close to"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor3 = "slightly lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor3 = "moderately lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor3 = "notably lower than"
    else:
        descriptor3 = "significantly lower than"

    if float(data[lowestNeighborhood][0]) > float(averageData2+1):
        descriptor4 = "significantly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.75):
        descriptor4 = "notably higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.5):
        descriptor4 = "moderately higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.25):
        descriptor4 = "slightly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2):
        descriptor4 = "close to"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.25):
        descriptor4 = "slightly lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.5):
        descriptor4 = "moderately lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.75):
        descriptor4 = "notably lower than"
    else:
        descriptor4 = "significantly lower than"

    if float(data[lowestNeighborhood2][0]) > float(averageData2+1):
        descriptor5 = "significantly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor5 = "notably higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor5 = "moderately higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor5 = "slightly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2):
        descriptor5 = "close to"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor5 = "slightly lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor5 = "moderately lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor5 = "notably lower than"
    else:
        descriptor5 = "significantly lower than"

    if float(boroughChange) > float(averageChange+0.4):
        descriptor6 = "significantly higher than"
        descriptor7 = "significantly high"
    elif float(boroughChange) > float(averageChange+0.3):
        descriptor6 = "notably higher than"
        descriptor7 = "notably high"
    elif float(boroughChange) > float(averageChange+0.2):
        descriptor6 = "moderately higher than"
        descriptor7 = "moderately high"
    elif float(boroughChange) > float(averageChange+0.1):
        descriptor6 = "slightly higher than"
        descriptor7 = "slightly high"
    elif float(boroughChange) > float(averageChange):
        descriptor6 = "close to"
        descriptor7 = "comparable"
    elif float(boroughChange) > float(averageChange-0.1):
        descriptor6 = "slightly lower than"
        descriptor7 = "slightly underwhelming"
    elif float(boroughChange) > float(averageChange-0.2):
        descriptor6 = "moderately lower than"
        descriptor7 = "moderately underwhelming"
    elif float(boroughChange) > float(averageChange-0.3):
        descriptor6 = "notably lower than"
        descriptor7 = "notably little"
    else:
        descriptor6 = "significantly lower than"
        descriptor7 = "significantly little"

    name=boroughs[2]

    return render_template('micro.html', aC=round(averageChange, 2), bC=round(boroughChange, 2), d6=descriptor6, d7=descriptor7, aD=round(averageData2, 1), bA=round(boroughAverage, 1), d1=descriptor1, hN=highestNeighborhood, d2=descriptor2, hN2=highestNeighborhood2, d3=descriptor3, lN=lowestNeighborhood, d4=descriptor4, lN2=lowestNeighborhood2, d5=descriptor5, name=name, fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+1)

@app.route('/queens')
def micro4():
    f = open("_data/nycMortality_area.json", "r")
    data = json.load(f)
    f.close()

    g = open("_data/nycMortality_borough.json", "r")
    data2 = json.load(g)
    g.close()

    boroughs = list(data2.keys())
    averageData = 0
    averageChange = 0

    for borough in boroughs:
        averageChange += (float(data2[borough][0])-float(data2[borough][9]))
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50
    averageChange = averageChange/5

    points = ""

    year = 2007
    for value in data2[boroughs[3]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    boroughChange = float(data2[boroughs[3]][0])-float(data2[boroughs[3]][9])
    points = points[:-1]

    neighborhoods = list(data.keys())

    fills = []

    highest = 0
    highest2 = 0
    lowest = 100
    lowest2 = 100

    highestNeighborhood = ''
    highestNeighborhood2 = ''
    lowestNeighborhood = ''
    lowestNeighborhood2 = ''

    averageData2 = 0
    boroughAverage = 0
    count = 0

    for neighborhood in neighborhoods:
        averageData2 += float(data[neighborhood][0])

        if data[neighborhood][1] != "4":
            fills.append("lightgray")
        else:
            boroughAverage += float(data[neighborhood][0])
            count += 1
            if 0 <= float(data[neighborhood][0]) < 1:
                fills.append("#ffcccc")
            elif 1 <= float(data[neighborhood][0]) < 1.25:
                fills.append("#ff9999")
            elif 1.25 <= float(data[neighborhood][0]) < 1.5:
                fills.append("#ff6666")
            elif 1.5 <= float(data[neighborhood][0]) < 1.75:
                fills.append("#ff3333")
            elif 1.75 <= float(data[neighborhood][0]) < 2:
                fills.append("#ff0000")
            elif 2 <= float(data[neighborhood][0]) < 2.25:
                fills.append("#cc0000")
            elif 2.25 <= float(data[neighborhood][0]) < 2.5:
                fills.append("#990000")
            elif 2.5 <= float(data[neighborhood][0]) < 2.75:
                fills.append("#660000")
            elif 2.75 <= float(data[neighborhood][0]) < 3:
                fills.append("#330000")
            elif 3 <= float(data[neighborhood][0]) <= 10:
                fills.append("#190000")

            if float(data[neighborhood][0]) > float(highest):
                highestNeighborhood2 = highestNeighborhood
                highestNeighborhood = neighborhood
                highest2 = highest
                highest = data[neighborhood][0]
            elif float(data[neighborhood][0]) > float(highest2):
                highestNeighborhood2 = neighborhood
                highest2 = data[neighborhood][0]

            if float(data[neighborhood][0]) < float(lowest):
                lowestNeighborhood2 = lowestNeighborhood
                lowestNeighborhood = neighborhood
                lowest2 = lowest
                lowest = data[neighborhood][0]
            elif float(data[neighborhood][0]) < float(lowest2):
                lowestNeighborhood2 = neighborhood
                lowest2 = data[neighborhood][0]
    
    averageData2 = averageData2/42
    boroughAverage = boroughAverage/count

    if float(boroughAverage) > float(averageData2+1):
        descriptor1 = "significantly higher than"
    elif float(boroughAverage) > float(averageData2+0.75):
        descriptor1 = "notably higher than"
    elif float(boroughAverage) > float(averageData2+0.5):
        descriptor1 = "moderately higher than"
    elif float(boroughAverage) > float(averageData2+0.25):
        descriptor1 = "slightly higher than"
    elif float(boroughAverage) > float(averageData2):
        descriptor1 = "close to"
    elif float(boroughAverage) > float(averageData2-0.25):
        descriptor1 = "slightly lower than"
    elif float(boroughAverage) > float(averageData2-0.5):
        descriptor1 = "moderately lower than"
    elif float(boroughAverage) > float(averageData2-0.75):
        descriptor1 = "notably lower than"
    else:
        descriptor1 = "significantly lower than"

    if float(data[highestNeighborhood][0]) > float(averageData2+1):
        descriptor2 = "significantly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.75):
        descriptor2 = "notably higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.5):
        descriptor2 = "moderately higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.25):
        descriptor2 = "slightly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2):
        descriptor2 = "close to"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.25):
        descriptor2 = "slightly lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.5):
        descriptor2 = "moderately lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.75):
        descriptor2 = "notably lower than"
    else:
        descriptor2 = "significantly lower than"

    if float(data[highestNeighborhood2][0]) > float(averageData2+1):
        descriptor3 = "significantly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor3 = "notably higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor3 = "moderately higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor3 = "slightly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2):
        descriptor3 = "close to"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor3 = "slightly lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor3 = "moderately lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor3 = "notably lower than"
    else:
        descriptor3 = "significantly lower than"

    if float(data[lowestNeighborhood][0]) > float(averageData2+1):
        descriptor4 = "significantly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.75):
        descriptor4 = "notably higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.5):
        descriptor4 = "moderately higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.25):
        descriptor4 = "slightly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2):
        descriptor4 = "close to"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.25):
        descriptor4 = "slightly lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.5):
        descriptor4 = "moderately lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.75):
        descriptor4 = "notably lower than"
    else:
        descriptor4 = "significantly lower than"

    if float(data[lowestNeighborhood2][0]) > float(averageData2+1):
        descriptor5 = "significantly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor5 = "notably higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor5 = "moderately higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor5 = "slightly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2):
        descriptor5 = "close to"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor5 = "slightly lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor5 = "moderately lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor5 = "notably lower than"
    else:
        descriptor5 = "significantly lower than"

    if float(boroughChange) > float(averageChange+0.4):
        descriptor6 = "significantly higher than"
        descriptor7 = "significantly high"
    elif float(boroughChange) > float(averageChange+0.3):
        descriptor6 = "notably higher than"
        descriptor7 = "notably high"
    elif float(boroughChange) > float(averageChange+0.2):
        descriptor6 = "moderately higher than"
        descriptor7 = "moderately high"
    elif float(boroughChange) > float(averageChange+0.1):
        descriptor6 = "slightly higher than"
        descriptor7 = "slightly high"
    elif float(boroughChange) > float(averageChange):
        descriptor6 = "close to"
        descriptor7 = "comparable"
    elif float(boroughChange) > float(averageChange-0.1):
        descriptor6 = "slightly lower than"
        descriptor7 = "slightly underwhelming"
    elif float(boroughChange) > float(averageChange-0.2):
        descriptor6 = "moderately lower than"
        descriptor7 = "moderately underwhelming"
    elif float(boroughChange) > float(averageChange-0.3):
        descriptor6 = "notably lower than"
        descriptor7 = "notably little"
    else:
        descriptor6 = "significantly lower than"
        descriptor7 = "significantly little"

    name=boroughs[3]

    return render_template('micro.html', aC=round(averageChange, 2), bC=round(boroughChange, 2), d6=descriptor6, d7=descriptor7, aD=round(averageData2, 1), bA=round(boroughAverage, 1), d1=descriptor1, hN=highestNeighborhood, d2=descriptor2, hN2=highestNeighborhood2, d3=descriptor3, lN=lowestNeighborhood, d4=descriptor4, lN2=lowestNeighborhood2, d5=descriptor5, name=name, fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+3.5)

@app.route('/staten')
def micro5():
    f = open("_data/nycMortality_area.json", "r")
    data = json.load(f)
    f.close()

    g = open("_data/nycMortality_borough.json", "r")
    data2 = json.load(g)
    g.close()

    boroughs = list(data2.keys())
    averageData = 0
    averageChange = 0

    for borough in boroughs:
        averageChange += (float(data2[borough][0])-float(data2[borough][9]))
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50
    averageChange = averageChange/5

    points = ""

    year = 2007
    for value in data2[boroughs[4]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    boroughChange = float(data2[boroughs[4]][0])-float(data2[boroughs[4]][9])
    points = points[:-1]

    neighborhoods = list(data.keys())

    fills = []

    highest = 0
    highest2 = 0
    lowest = 100
    lowest2 = 100

    highestNeighborhood = ''
    highestNeighborhood2 = ''
    lowestNeighborhood = ''
    lowestNeighborhood2 = ''

    averageData2 = 0
    boroughAverage = 0
    count = 0

    for neighborhood in neighborhoods:
        averageData2 += float(data[neighborhood][0])

        if data[neighborhood][1] != "5":
            fills.append("lightgray")
        else:
            boroughAverage += float(data[neighborhood][0])
            count += 1
            if 0 <= float(data[neighborhood][0]) < 1:
                fills.append("#ffcccc")
            elif 1 <= float(data[neighborhood][0]) < 1.25:
                fills.append("#ff9999")
            elif 1.25 <= float(data[neighborhood][0]) < 1.5:
                fills.append("#ff6666")
            elif 1.5 <= float(data[neighborhood][0]) < 1.75:
                fills.append("#ff3333")
            elif 1.75 <= float(data[neighborhood][0]) < 2:
                fills.append("#ff0000")
            elif 2 <= float(data[neighborhood][0]) < 2.25:
                fills.append("#cc0000")
            elif 2.25 <= float(data[neighborhood][0]) < 2.5:
                fills.append("#990000")
            elif 2.5 <= float(data[neighborhood][0]) < 2.75:
                fills.append("#660000")
            elif 2.75 <= float(data[neighborhood][0]) < 3:
                fills.append("#330000")
            elif 3 <= float(data[neighborhood][0]) <= 10:
                fills.append("#190000")

            if float(data[neighborhood][0]) > float(highest):
                highestNeighborhood2 = highestNeighborhood
                highestNeighborhood = neighborhood
                highest2 = highest
                highest = data[neighborhood][0]
            elif float(data[neighborhood][0]) > float(highest2):
                highestNeighborhood2 = neighborhood
                highest2 = data[neighborhood][0]

            if float(data[neighborhood][0]) < float(lowest):
                lowestNeighborhood2 = lowestNeighborhood
                lowestNeighborhood = neighborhood
                lowest2 = lowest
                lowest = data[neighborhood][0]
            elif float(data[neighborhood][0]) < float(lowest2):
                lowestNeighborhood2 = neighborhood
                lowest2 = data[neighborhood][0]
    
    averageData2 = averageData2/42
    boroughAverage = boroughAverage/count

    if float(boroughAverage) > float(averageData2+1):
        descriptor1 = "significantly higher than"
    elif float(boroughAverage) > float(averageData2+0.75):
        descriptor1 = "notably higher than"
    elif float(boroughAverage) > float(averageData2+0.5):
        descriptor1 = "moderately higher than"
    elif float(boroughAverage) > float(averageData2+0.25):
        descriptor1 = "slightly higher than"
    elif float(boroughAverage) > float(averageData2):
        descriptor1 = "close to"
    elif float(boroughAverage) > float(averageData2-0.25):
        descriptor1 = "slightly lower than"
    elif float(boroughAverage) > float(averageData2-0.5):
        descriptor1 = "moderately lower than"
    elif float(boroughAverage) > float(averageData2-0.75):
        descriptor1 = "notably lower than"
    else:
        descriptor1 = "significantly lower than"

    if float(data[highestNeighborhood][0]) > float(averageData2+1):
        descriptor2 = "significantly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.75):
        descriptor2 = "notably higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.5):
        descriptor2 = "moderately higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2+0.25):
        descriptor2 = "slightly higher than"
    elif float(data[highestNeighborhood][0]) > float(averageData2):
        descriptor2 = "close to"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.25):
        descriptor2 = "slightly lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.5):
        descriptor2 = "moderately lower than"
    elif float(data[highestNeighborhood][0]) > float(averageData2-0.75):
        descriptor2 = "notably lower than"
    else:
        descriptor2 = "significantly lower than"

    if float(data[highestNeighborhood2][0]) > float(averageData2+1):
        descriptor3 = "significantly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor3 = "notably higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor3 = "moderately higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor3 = "slightly higher than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2):
        descriptor3 = "close to"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor3 = "slightly lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor3 = "moderately lower than"
    elif float(data[highestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor3 = "notably lower than"
    else:
        descriptor3 = "significantly lower than"

    if float(data[lowestNeighborhood][0]) > float(averageData2+1):
        descriptor4 = "significantly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.75):
        descriptor4 = "notably higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.5):
        descriptor4 = "moderately higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2+0.25):
        descriptor4 = "slightly higher than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2):
        descriptor4 = "close to"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.25):
        descriptor4 = "slightly lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.5):
        descriptor4 = "moderately lower than"
    elif float(data[lowestNeighborhood][0]) > float(averageData2-0.75):
        descriptor4 = "notably lower than"
    else:
        descriptor4 = "significantly lower than"

    if float(data[lowestNeighborhood2][0]) > float(averageData2+1):
        descriptor5 = "significantly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.75):
        descriptor5 = "notably higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.5):
        descriptor5 = "moderately higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2+0.25):
        descriptor5 = "slightly higher than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2):
        descriptor5 = "close to"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.25):
        descriptor5 = "slightly lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.5):
        descriptor5 = "moderately lower than"
    elif float(data[lowestNeighborhood2][0]) > float(averageData2-0.75):
        descriptor5 = "notably lower than"
    else:
        descriptor5 = "significantly lower than"

    if float(boroughChange) > float(averageChange+0.4):
        descriptor6 = "significantly higher than"
        descriptor7 = "significantly high"
    elif float(boroughChange) > float(averageChange+0.3):
        descriptor6 = "notably higher than"
        descriptor7 = "notably high"
    elif float(boroughChange) > float(averageChange+0.2):
        descriptor6 = "moderately higher than"
        descriptor7 = "moderately high"
    elif float(boroughChange) > float(averageChange+0.1):
        descriptor6 = "slightly higher than"
        descriptor7 = "slightly high"
    elif float(boroughChange) > float(averageChange):
        descriptor6 = "close to"
        descriptor7 = "comparable"
    elif float(boroughChange) > float(averageChange-0.1):
        descriptor6 = "slightly lower than"
        descriptor7 = "slightly underwhelming"
    elif float(boroughChange) > float(averageChange-0.2):
        descriptor6 = "moderately lower than"
        descriptor7 = "moderately underwhelming"
    elif float(boroughChange) > float(averageChange-0.3):
        descriptor6 = "notably lower than"
        descriptor7 = "notably little"
    else:
        descriptor6 = "significantly lower than"
        descriptor7 = "significantly little"

    name=boroughs[4]

    return render_template('micro.html', aC=round(averageChange, 2), bC=round(boroughChange, 2), d6=descriptor6, d7=descriptor7, aD=round(averageData2, 1), bA=round(boroughAverage, 1), d1=descriptor1, hN=highestNeighborhood, d2=descriptor2, hN2=highestNeighborhood2, d3=descriptor3, lN=lowestNeighborhood, d4=descriptor4, lN2=lowestNeighborhood2, d5=descriptor5, name=name, fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+3.5)

app.run(debug=True, port=6060)