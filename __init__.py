# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:01:42 2019

@author: zhaih
"""
import flask
from flask import Flask

app = Flask(__name__)

from app import routes