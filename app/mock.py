# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:02:26 2019

@author: ottil
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask("MyApp")
cors = CORS(app)


@app.route("/")
def index():
    data={
            'Monday': [{'id': 1, 'title': 'Homework', 'date': '2019-02-18', 'day': 'Monday', 'time': '11:30:00', 'description': 'Do python chapter 1', 'priority': 'high', 'status': 'complete'}], 
            'Tuesday': [], 
            'Wednesday': [{'id': 2, 'title': 'Dinner', 'date': '2019-02-20', 'day': 'Wednesday', 'time': '11:30:00', 'description': 'Make dinner', 'priority': 'medium', 'status': 'incomplete'}], 
            'Thursday': [{'id': 3, 'title': 'Clean', 'date': '2019-02-21', 'day': 'Thursday', 'time': '10:15:00', 'description': 'Clean kitchen and living room', 'priority': 'low', 'status': 'incomplete'}], 
            'Friday': [], 
            'Saturday': [], 
            'Sunday': [{'id': 7, 'title': 'Sleep', 'date': '2019-02-21', 'day': 'Thursday', 'time': '10:15:00', 'description': 'Clean kitchen and living room', 'priority': 'low', 'status': 'incomplete'}], 
            'high': [{'id': 1, 'title': 'Homework', 'date': '2019-02-18', 'day': 'Monday', 'time': '11:30:00', 'description': 'Do python chapter 1', 'priority': 'high', 'status': 'complete'}], 
            'due': [{'id': 2, 'title': 'Dinner', 'date': '2019-02-20', 'day': 'Wednesday', 'time': '11:30:00', 'description': 'Make dinner', 'priority': 'medium', 'status': 'incomplete'}]}
    return render_template("index.html", data=data)
  
@app.route("/api")
def index_api():
    data={'Monday': [{'id': 1, 'title': 'Homework', 'date': '2019-02-18', 'day': 'Monday', 'time': '11:30:00', 'description': 'Do python chapter 1', 'priority': 'high', 'status': 'complete'}], 'Tuesday': [], 'Wednesday': [{'id': 2, 'title': 'Dinner', 'date': '2019-02-20', 'day': 'Wednesday', 'time': '11:30:00', 'description': 'Make dinner', 'priority': 'medium', 'status': 'incomplete'}], 'Thursday': [{'id': 3, 'title': 'Clean', 'date': '2019-02-21', 'day': 'Thursday', 'time': '10:15:00', 'description': 'Clean kitchen and living room', 'priority': 'low', 'status': 'incomplete'}], 'Friday': [], 'Saturday': [], 'Sunday': [], 'high': [{'id': 1, 'title': 'Homework', 'date': '2019-02-18', 'day': 'Monday', 'time': '11:30:00', 'description': 'Do python chapter 1', 'priority': 'high', 'status': 'complete'}], 'due': [{'id': 2, 'title': 'Dinner', 'date': '2019-02-20', 'day': 'Wednesday', 'time': '11:30:00', 'description': 'Make dinner', 'priority': 'medium', 'status': 'incomplete'}]}
    data=jsonify(data)
    return data

if __name__=='__main__':
    app.run(debug=True)