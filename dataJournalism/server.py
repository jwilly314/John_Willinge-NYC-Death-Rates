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

@app.route('/micro')
def micro():
    return render_template('micro.html')

@app.route('/macro')
def macro():
    return render_template('macro.html')

app.run(debug=True, port=6060)