#!/usr/bin/env python
"""Where the f*** shall we go?
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import pytz
from datetime import datetime

TIMEZONE = pytz.timezone('Europe/London')
PUBS = open('pubs.txt').read().splitlines()

def create_app():
    app = Flask(__name__)
    Bootstrap(app)  
    return app

app = create_app()

@app.route('/')
def index():
    # Parse the date
    date = request.args.get('date', default='', type=str)
    if date == '':
        mydate = datetime.now(TIMEZONE)
    else:
        mydate = datetime.strptime(date, '%d/%m/%Y')
    day_of_year = mydate.timetuple().tm_yday

    mypub = PUBS[day_of_year % len(PUBS)]
    return render_template('index.html',
                           date=date,
                           pub=mypub)


if __name__ == "__main__":
    app.run(debug=True)
