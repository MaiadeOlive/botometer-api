#!/usr/bin/env python
# -*- coding: utf-8 -*-
import botometer
import os
import json
import shutil
from datetime import datetime
import glob


def check_if_bot(accounts):

    path = 'results/'
    d = datetime.now()
    final_zip_path = 'requisition/' + str(d.date()) 

    rapidapi_key = os.environ.get('RAPIDAPI_KEY')
        
    twitter_app_auth = {
        'consumer_key': os.environ.get('CONSUMER_KEY'), 
        'consumer_secret': os.environ.get('CONSUMER_SECRET'),
        'access_token': os.environ.get('ACCESS_TOKEN'),
        'access_token_secret': os.environ.get('ACCESS_TOKEN_SECRET'),
    }

    bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)

    for screen_name, result in bom.check_accounts_in(accounts):
        file_path = path + screen_name + '.txt'
        with open(file_path, 'a') as f:
            f.write(str(json.dumps(result, indent=4, sort_keys=True)))

    shutil.make_archive(final_zip_path, 'zip', path)

    lista_path = glob.glob('/results/')
    for i in lista_path:
        os.remove(i)
    