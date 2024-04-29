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
    print(neighborhoods)
    requested_data = {}
    for neighborhood in neighborhoods:
        requested_data[neighborhood] = data[neighborhood]

    fills = []
    for neighborhood in neighborhoods:
        if 0.5 <= float(data[neighborhood][0]) < 0.75:
            fills.append("#ff0000")
        elif 0.75 <= float(data[neighborhood][0]) < 1:
            fills.append("#e60000")
        elif 1 <= float(data[neighborhood][0]) < 1.25:
            fills.append("#cc0000")
        elif 1.25 <= float(data[neighborhood][0]) < 1.5:
            fills.append("#b30000")
        elif 1.5 <= float(data[neighborhood][0]) < 1.75:
            fills.append("#990000")
        elif 1.75 <= float(data[neighborhood][0]) < 2:
            fills.append("#800000")
        elif 2 <= float(data[neighborhood][0]) < 2.25:
            fills.append("#660000")
        elif 2.25 <= float(data[neighborhood][0]) < 2.5:
            fills.append("#4d0000")
        elif 2.5 <= float(data[neighborhood][0]) < 2.75:
            fills.append("#330000")
        elif 2.75 <= float(data[neighborhood][0]) < 3:
            fills.append("#190000")
    print(fills)

    return render_template('macro.html', data=requested_data, fills=fills)


@app.route('/manhattan')
def micro1():
    return render_template('microManhattan.html')

@app.route('/bronx')
def micro2():
    return render_template('microBronx.html')

@app.route('/queens')
def micro3():
    return render_template('microQueens.html')

@app.route('/brooklyn')
def micro4():
    return render_template('microBrooklyn.html')

@app.route('/staten')
def micro5():
    return render_template('microStaten.html')

app.run(debug=True, port=6060)