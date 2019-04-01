from flask import Flask
from flask import render_template
import json
from config import Config
import pymongo

SC = Config.SC

app = Flask(__name__)

@app.route('/')
def sc():
    return 'Hello World!'

@app.route('/<int:year>')
def show_year(year):

    results = SC.find({'year': year})

    return render_template('sc_table.html', results=results, year=year) 

if __name__ == '__main__':
        app.run(debug=True)