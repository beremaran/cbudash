#!/usr/bin/env python3

from flask import Flask
from flask import jsonify, render_template

from cbudash.dash import CBUDash

app = Flask(__name__)
cbu_dash = CBUDash()


@app.route('/')
def index():
    return render_template('index.html', news=cbu_dash.get())


@app.route('/feed.json')
def feed():
    return jsonify(cbu_dash.get())


if __name__ == '__main__':
    app.run()
