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
    requested_data = {}
    for neighborhood in neighborhoods:
        requested_data[neighborhood] = data[neighborhood]

    if 0.5 <= float(data["Kingsbridge - Riverdale"][0]) < 0.75:
        fill1 = "#ff0000"
    elif 0.75 <= float(data["Kingsbridge - Riverdale"][0]) < 1:
        fill1 = "#e60000"
    elif 1 <= float(data["Kingsbridge - Riverdale"][0]) < 1.25:
        fill1 = "#cc0000"
    elif 1.23 <= float(data["Kingsbridge - Riverdale"][0]) < 1.5:
        fill1 = "#b30000"
    elif 1.5 <= float(data["Kingsbridge - Riverdale"][0]) < 1.75:
        fill1 = "#990000"
    elif 1.75 <= float(data["Kingsbridge - Riverdale"][0]) < 2:
        fill1 = "#800000"
    elif 2 <= float(data["Kingsbridge - Riverdale"][0]) < 2.25:
        fill1 = "#660000"
    elif 2.25 <= float(data["Kingsbridge - Riverdale"][0]) < 2.5:
        fill1 = "#4d0000"
    elif 2.5 <= float(data["Kingsbridge - Riverdale"][0]) < 2.75:
        fill1 = "#330000"
    elif 2.75 <= float(data["Kingsbridge - Riverdale"][0]) < 3:
        fill1 = "#190000"

    return render_template('macro.html', data=requested_data, fill1=fill1)


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