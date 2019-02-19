# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:14:58 2019

@author: amina
"""

import json
import sqlite3
import requests
import datetime
import calendar

db_path ='static/db/tasks.db'

def getdb():
    conn=sqlite3.connect(db_path)
    c=conn.cursor()
    return (c,conn)

def create_table():
    c,conn=getdb()
    c.execute('CREATE TABLE IF NOT EXISTS tasks (id REAL, title TEXT, date DATE, day TEXT,time TIME, description TEXT, priority TEXT, status TEXT)')

def convert_date_to_day(date):
    year, month, day = (int(x) for x in date.split('-'))
    answer = datetime.date(year, month, day).weekday()
    day = calendar.day_name[answer]
    return day
 
def data_entry(id_t,title,date,time,description,priority,status):
    day = convert_date_to_day(date)
    c,conn=getdb()
    c.execute("INSERT INTO tasks VALUES(?,?,?,?,?,?,?,?)",(id_t,title,date,day,time,description,priority,status))
    conn.commit() 
    c.close() 
    conn.close() 
    
def delete_task(id_t):
    c,conn=getdb()
    c.execute('DELETE FROM tasks WHERE id=?',(id_t,))
    conn.commit()
    
def edit_task(id_t,title,date,time,description,priority,status):
    c,conn=getdb()
    c.execute('DELETE FROM tasks WHERE id=?',(id_t,))
    data_entry(id_t,title,date,time,description,priority,status)
    conn.commit()

def retrieve_data(query):
    c,conn=getdb()
    c.execute(query)
    response=c.fetchall()
    data={'tasks':[]}
    for row in response:
        data['tasks'].append({'id':row[0],'title':row[1],'date':row[2],'day':row[3],'time':row[4],'description':row[5],'priority':row[6],'status':row[7]})
    data = json.dumps(data)
    return data
    
def retrieve_all_tasks():
    query = 'SELECT * FROM tasks ORDER BY date'
    data = retrieve_data(query)
    return data

def retrieve_a_task(id_t):
    query = 'SELECT * FROM tasks WHERE id=1'.format(id_t)
    data = retrieve_data(query)
    return data

def call_api(payload):
    endpoint = 'http://127.0.0.1:5000/'
    response = requests.get(endpoint+payload)
    data = response.json()  
    data = groupBy_day(data)
    return data    

def groupBy_day(data):
    date_today=datetime.datetime.today().strftime('%Y-%m-%d')
    d_group={'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[],'Saturday':[],'Sunday':[],'high':[],'due':[]}
    for d in data['tasks']:
        if d['day'] == 'Monday':
            d_group['Monday'].append(d)
        if d['day'] == 'Tuesday':
            d_group['Tuesday'].append(d)
        if d['day'] == 'Wednesday':
            d_group['Wednesday'].append(d)
        if d['day'] == 'Thursday':
            d_group['Thursday'].append(d)
        if d['day'] == 'Friday':
            d_group['Friday'].append(d)
        if d['day'] == 'Saturday':
            d_group['Saturday'].append(d)
        if d['day'] == 'Sunday':
            d_group['Saturday'].append(d)
        if d['priority'] == 'high':
            d_group['high'].append(d)
        if d['date'] == date_today:
            d_group['due'].append(d)
    return d_group

def status_process(status_l):
    print(status_l)


            
    

    

