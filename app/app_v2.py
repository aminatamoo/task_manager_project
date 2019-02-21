# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:53:46 2019

@author: ottil
"""

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_cors import CORS
from api import *
import requests

app = Flask("MyApp")
cors = CORS(app)
app.config['SECRET_KEY'] = 'reds209ndsldssdsljdslddbfudfbidabdfnfsfis'
#app.secret_key()

#    
##-----------------HTML TEMPLATE--------------#
@app.route("/index",methods=['GET','POST'])
def index():
    payload='alltasks'
    data=call_api_alltask(payload)
    if request.method=='POST':
        status =request.form.getlist('check')
        status_process(status,data)
        return redirect(url_for('index'))            
    if request.method=='GET':
        return render_template('index2.html',data=data)

@app.route("/showtask/<id_t>",methods=['GET','POST'])
def showtask(id_t):
    payload='task/{}'.format(id_t)
    data=call_api_onetask(payload)
    id_t=id_t
    title=data['tasks'][0]['title']
    date=data['tasks'][0]['date']
    time=data['tasks'][0]['time']
    description=data['tasks'][0]['description']
    priority=data['tasks'][0]['priority']
    status=data['tasks'][0]['status']
    if request.method=='POST':
        if request.form['edit_button']=='Edit Task':
            return redirect(url_for('edittask', id_t=id_t))
        if request.form['delete_button']=='Delete Task':
            delete_task(id_t)
            return redirect(url_for('index'))
        if request.form['close_button']=='Close Task':
            return redirect(url_for('index'))
            
    if request.method=='GET':
        return render_template('showtask_v1.html',**locals())

@app.route("/edittask/<id_t>",methods=['GET','POST'])
def edittask(id_t):
    payload='task/{}'.format(id_t)
    data=call_api_onetask(payload)
    id_t=id_t
    title=data['tasks'][0]['title']
    date=data['tasks'][0]['date']
    time=data['tasks'][0]['time']
    description=data['tasks'][0]['description']
    priority=data['tasks'][0]['priority']
    status=data['tasks'][0]['status']
    if request.method=='POST':
        pass      
    if request.method=='GET':
        return render_template('edittask_v1.html',**locals()) 
    
@app.route("/addtask",methods=['GET','POST'])
def addtask():
    if request.method=='POST':

        title=request.form['title']
        date=request.form['date']
        time=request.form['time']
        priority=request.form['priority']
        description=request.form['description']
        data_entry(title, date, time, description, priority)
        flash('You\'ve successfully added a task', 'success')       
        return redirect(url_for('index'))
    if request.method=='GET':
        return render_template('addtask.html',**locals())
 
#----------------API URLS--------------------#
 
@app.route("/alltasks")
def alltasks():
    data = retrieve_all_tasks()
    return data
        
@app.route("/task/<int:id_t>")
def task_id(id_t):
    data = retrieve_a_task(id_t) 
    return data


#@app.route('/addtask',methods=['GET','POST'])
#def addtask():
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