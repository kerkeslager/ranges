import json
import os
from bottle import route, run, template

@route('/')
def index():
    ranges = os.listdir('ranges')
    print(ranges)
    return template('index.html', ranges=ranges)

RANKS = 'AKQJT98765432'

@route('/r/<name>')
def range_view(name):
    with open('ranges/{}.json'.format(name), 'r') as f:
        _range = json.load(f)
    return template('range.html', _range=_range['range'], RANKS=RANKS)

run(host='localhost', port=8080)
