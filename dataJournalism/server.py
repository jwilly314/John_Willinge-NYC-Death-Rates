# flask --app data_server run
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

@app.route('/macro')
def macro():
    f = open("_data/nycMortality_area.json", "r")
    data = json.load(f)
    f.close()

    #Filter and reformat data for ease of access in the template
    neighborhoods = list(data.keys())

    fills = []
    for neighborhood in neighborhoods:
        if 0 <= float(data[neighborhood][0]) < 1:
            fills.append("#ff0000")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#e60000")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#cc0000")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#b30000")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#990000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#800000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#660000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#4d0000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#330000")
        elif 3 <= float(data[neighborhood][0]) <= 10:
            fills.append("#190000")

    return render_template('macro.html', data=data, fills=fills)

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

    for borough in boroughs:
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50

    points = ""

    year = 2007
    for value in data2[boroughs[0]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    points = points[:-1]

    #Filter and reformat data for ease of access in the template
    neighborhoods = list(data.keys())

    fills = []
    for neighborhood in neighborhoods:
        if 0 <= float(data[neighborhood][0]) < 1:
            fills.append("#ff0000")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#e60000")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#cc0000")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#b30000")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#990000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#800000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#660000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#4d0000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#330000")
        elif 3 <= float(data[neighborhood][0]) <= 10:
            fills.append("#190000")

    name=boroughs[0]

    return render_template('micro.html', name=name, map=name+'.svg', fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+5.5)

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

    for borough in boroughs:
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50

    points = ""

    year = 2007
    for value in data2[boroughs[1]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    points = points[:-1]

    #Filter and reformat data for ease of access in the template
    neighborhoods = list(data.keys())

    fills = []
    for neighborhood in neighborhoods:
        if 0 <= float(data[neighborhood][0]) < 1:
            fills.append("#ff0000")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#e60000")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#cc0000")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#b30000")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#990000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#800000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#660000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#4d0000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#330000")
        elif 3 <= float(data[neighborhood][0]) <= 10:
            fills.append("#190000")

    name=boroughs[1]

    return render_template('micro.html', name=name, map=name+'.svg', fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)-0.5)

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

    for borough in boroughs:
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50

    points = ""

    year = 2007
    for value in data2[boroughs[2]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    points = points[:-1]

    #Filter and reformat data for ease of access in the template
    neighborhoods = list(data.keys())

    fills = []
    for neighborhood in neighborhoods:
        if 0 <= float(data[neighborhood][0]) < 1:
            fills.append("#ff0000")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#e60000")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#cc0000")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#b30000")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#990000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#800000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#660000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#4d0000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#330000")
        elif 3 <= float(data[neighborhood][0]) <= 10:
            fills.append("#190000")

    name=boroughs[2]

    return render_template('micro.html', name=name, map=name+'.svg', fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+1)

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

    for borough in boroughs:
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50

    points = ""

    year = 2007
    for value in data2[boroughs[3]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    points = points[:-1]

    #Filter and reformat data for ease of access in the template
    neighborhoods = list(data.keys())

    fills = []
    for neighborhood in neighborhoods:
        if 0 <= float(data[neighborhood][0]) < 1:
            fills.append("#ff0000")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#e60000")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#cc0000")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#b30000")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#990000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#800000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#660000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#4d0000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#330000")
        elif 3 <= float(data[neighborhood][0]) <= 10:
            fills.append("#190000")

    name=boroughs[3]

    return render_template('micro.html', name=name, map=name+'.svg', fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+3.5)

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

    for borough in boroughs:
        for value in data2[borough]:
            averageData += float(value)

    averageData = averageData/50

    points = ""

    year = 2007
    for value in data2[boroughs[4]]:
        points = points + str(40+((year-2007)*23.3333)) + "," + str(260-(float(value))*20) + " "
        year += 1
        if year==2016:
            finalPoint = str(260-(float(value))*20)

    points = points[:-1]

    #Filter and reformat data for ease of access in the template
    neighborhoods = list(data.keys())

    fills = []
    for neighborhood in neighborhoods:
        if 0 <= float(data[neighborhood][0]) < 1:
            fills.append("#ff0000")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#e60000")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#cc0000")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#b30000")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#990000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#800000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#660000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#4d0000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#330000")
        elif 3 <= float(data[neighborhood][0]) <= 10:
            fills.append("#190000")

    name=boroughs[4]
            
    return render_template('micro.html', name=name, map=name+'.svg', fills=fills, data=data, data2=data2, averageData = 260-(averageData*20), numericalAverage=averageData, points=points, finalPoint=float(finalPoint)+3.5)

app.run(debug=True, port=6060)