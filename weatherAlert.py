# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:37:27 2019

@author: zhaih
"""
from app import app
import requests
import pprint


my_url = 'http://api.weather.com/v3/alerts/headlines'
my_params = {
        'adminDistrictCode' : "LA:US",
        'format' : "json",
        'language' : "en-US",
        'apiKey' : "da328055e2e940d8b28055e2e9e0d851"
        }



r = requests.get(url = my_url, params = my_params)
print(r)

print(r.json())