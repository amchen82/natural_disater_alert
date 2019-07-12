# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:04:10 2019

@author: zhaih
"""
import requests
import pprint
from app import app

@app.route('/')
@app.route('/index')
def index():
    my_url = 'http://api.weather.com/v3/alerts/headlines'
    my_params = {
        'adminDistrictCode' : "LA:US",
        'format' : "json",
        'language' : "en-US",
        'apiKey' : "da328055e2e940d8b28055e2e9e0d851"
        }

    my_params2 = {
        'adminDistrictCode' : "LA:US",
        'format' : "json",
        'language' : "en-es",
        'apiKey' : "da328055e2e940d8b28055e2e9e0d851"
        }

    r = requests.get(url = my_url, params = my_params)
    r2 = requests.get(url = my_url, params = my_params2)
    res = r.json()
    str_res=""
    alert =res['alerts'][0]
    str_res+=f"{alert['officeName']},{alert['eventDescription']}, {alert['severity']}, {alert['officeCountryCode']}"
    str_res+=res2['alerts'][0]
    
    
    
    translate_url = "https://gateway.watsonplatform.net/language-translator/api/v3/translate?version=2018-05-01"
    translate_apiKey = "utTGF8As_t_A6aaP-jibEUEwwQk7c3CThCzdHGYy7znQ"
    translate_data = {
            'text' : str_res,
            'model_id' : 'en-es'
            }
    
    
    #t = requests.post(url = translate_url, 
                      #data = translate_data, 
                      #headers={
                       
                      #"apikey":translate_apiKey,
#                              "Authorization" : f"Basic {translate_apiKey}",
                       #       "Content-Type" : "application/json"
                        #      })
   # print(t)
    
    
    return str_res #"hi"  #str(r.json()) #"Hello, World!"



#curl -X POST -u "apikey:{apikey}" --header "Content-Type: text/plain" --data "Language Translator translates text from one language to another" "{url}/v3/identify?version=2018-05-01"
