# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:53:46 2019

@author: ottil
"""

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_cors import CORS
from api import *
from config import key
import requests

app = Flask("MyApp")
cors = CORS(app)
app.config['SECRET_KEY'] = key
#app.secret_key()

   
#--------------------HTML TEMPLATE--------------------#

@app.route("/index",methods=['GET','POST'])
def index():
    payload='alltasks'
    data=call_api_alltask(payload)
    if request.method=='POST':
        if 'save' in request.form:
            status = request.form.getlist('check')
            status_process(status,data)
            flash('Your changes have been made successfully', 'success')
            return redirect(url_for('index'))
        if 'add' in request.form:
           return redirect(url_for('addtask'))         
    if request.method=='GET':
        return render_template('index.html',data=data)


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
        if 'edit' in request.form:
            return redirect(url_for('edittask', id_t=id_t))
        elif 'delete' in request.form:
            delete_task(id_t)
            flash('You\'ve successfully deleted a task', 'success')  
            return redirect(url_for('index'))
        elif 'close' in request.form:
            return redirect(url_for('index'))            
    if request.method=='GET':
        return render_template('showtask.html',**locals())


@app.route("/edittask/<id_t>",methods=['GET','POST'])
def edittask(id_t):
    if request.method=='POST':
        if 'save' in request.form:
            title=request.form.get('title')
            date=request.form.get('date')
            time=request.form.get('time')
            description=request.form.get('description')
            priority=request.form.get('priority')
            if request.form.get('status'):
                status='complete'
            elif not request.form.get('status'):
                status='incomplete'
            update_task(id_t,title,date,time,description,priority,status)           
            flash('You\'ve successfully updated a task', 'success')       
            return redirect(url_for('index'))
        elif 'delete' in request.form:
            delete_task(id_t)
            flash('You\'ve successfully deleted a task', 'success')       
            return redirect(url_for('index'))
        return render_template('edittask_v1.html')     
    if request.method=='GET':
        payload='task/{}'.format(id_t)
        data=call_api_onetask(payload)
        id_t=id_t
        title=data['tasks'][0]['title']
        date=data['tasks'][0]['date']
        time=data['tasks'][0]['time']
        description=data['tasks'][0]['description']
        priority=data['tasks'][0]['priority']
        status=data['tasks'][0]['status']
        return render_template('edittask.html',**locals()) 

    
@app.route("/addtask",methods=['GET','POST'])
def addtask():
    if request.method=='POST':
        title=request.form.get('title')
        date=request.form.get('date')
        time=request.form.get('time')
        priority=request.form.get('priority')    
        description=request.form.get('description')
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





if __name__=='__main__':
    app.run(debug=True)