from flask import render_template
from app import app
from flask import Response
import os

# home route


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', color='blues', pad='p-0')

# javascript


@app.route("/toggle_js")
def toggle_js():
    return render_template("/javascript/toggles.js")

# csv


@app.route("/csv")
def get_csv():
    path = os.path.abspath(os.path.dirname(__file__)) + '/pokemon.csv'
    with open(path, "r") as f:
        content = f.read()
    return Response(content, mimetype="text/plain")
