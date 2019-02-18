# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:53:46 2019

@author: ottil
"""

from flask import Flask, render_template, request
from engine import *

app = Flask("MyApp")

@app.route("/")

def index():
    return render_template("index.html")