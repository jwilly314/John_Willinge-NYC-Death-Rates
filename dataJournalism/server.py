# flask --app data_server run
from flask import Flask
from flask import render_template
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
    return render_template('macro.html')

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