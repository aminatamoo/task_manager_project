# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:53:46 2019

@author: ottil
"""

from flask import Flask, render_template, request, jsonify, flash, redirect
from flask_cors import CORS
from api import *
import requests

app = Flask("MyApp")
cors = CORS(app)

#    
##-----------------HTML TEMPLATE--------------#
@app.route("/index",methods=['GET','POST'])
def index():
    if request.method=='POST':
        status =request.form.getlist('check')
        if status!=None:
            status_process(status)
            print(type(status))
            return jsonify({'status':'ok'}) 
#        else:
#            return redirect('/addtask')
              
    if request.method=='GET':
        payload='all_tasks'
        data=call_api(payload)
        return render_template('index2.html',data=data)
 
#----------------API URLS--------------------#
 
@app.route("/all_tasks")
def all_tasks():
    data = retrieve_all_tasks()
    return data
        
@app.route("/task/<int:id_t>")
def task_id(id_t):
    data = retrieve_a_task(id_t) 
    return data


#@app.route('/addtask',methods=['GET','POST'])
#def get_data():
#    if request.method=='POST':
#        title=request.form['title']
#        date=request.form['date']
#        time=request.form['time']
#        priority=request.form['priority']
#        description=request.form['description']
#        dynamic_data_entry(title, date, time, priority, description)
#        flash('You\'ve successfully added a task')
#        return jsonify({'status':'ok'}
#    if request.method=='GET':
#        return render_template("addtask.html")
#    
#@app.route('/deltask',methods=['GET','POST'])
#def get_data():
#    if request.method=='POST':
#        title=request.form['title']
#        date=request.form['date']
#        time=request.form['time']
#        priority=request.form['priority']
#        description=request.form['description']
#        dynamic_data_entry(title, date, time, priority, description)
#        flash('You\'ve successfully added a task')
#        return redirect('/index')
#    if request.method=='GET':
#        return render_template("addtask.html")


if __name__=='__main__':
    app.run(debug=True)