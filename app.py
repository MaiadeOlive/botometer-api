# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for, send_file
from check_bot import check_if_bot
import os
from functools import wraps
from datetime import datetime
import csv

app = Flask(__name__)


def check_credencials(f):
    @wraps(f)
    def wrap(*args, **kwargs):

        alert = 'Por favor adicione as chaves da API'

        if os.environ.get('RAPIDAPI_KEY') is None:
            return render_template('index.html', alert=alert)

        return f(*args, **kwargs)

    return wrap


@app.route('/', methods=['GET'])
def index():
    return 'server'
    #return render_template('index.html')


@app.route('/conf', methods=['POST'])
def conf():

    alert2 = 'Sucesso'

    RAPIDAPI_KEY = request.form['rapidapi_key']
    CONSUMER_KEY = request.form['consumer_key']
    CONSUMER_SECRET = request.form['consumer_secret']
    ACCESS_TOKEN = request.form['access_token']
    ACCESS_TOKEN_SECRET = request.form['access_token_secret']

    os.environ["RAPIDAPI_KEY"] = RAPIDAPI_KEY
    os.environ["CONSUMER_KEY"] = CONSUMER_KEY
    os.environ["CONSUMER_SECRET"] = CONSUMER_SECRET
    os.environ["ACCESS_TOKEN"] = ACCESS_TOKEN
    os.environ["ACCESS_TOKEN_SECRET"] = ACCESS_TOKEN_SECRET

    return render_template('index.html', alert2=alert2)

@app.route('/get_twitter', methods=['POST'])
@check_credencials

def get_twitter():
    process_done = ''
    
    render_template('index.html', process_done=process_done)
    
    request_screen_name = request.form['screen_name']

    screen_names = request_screen_name.split(' ')

    check_if_bot(screen_names)

    process_done = 'Download Disponível'

    return render_template('index.html', process_done=process_done)

@app.route('/download_zip/', methods=['GET'])
@check_credencials
def download_zip():
    d = datetime.now()

    path = 'requisition/' + str(d.date()) + '.zip'
    
    return send_file(path, as_attachment=True) 
    

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)), host='0.0.0.0')

