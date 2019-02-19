# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:47:47 2019

@author: ottil
"""

import sqlite3
import json 
import datetime
import calendar

db_path ='static/tasks.db'

conn = sqlite3.connect('tasks.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasks (id INT, title TEXT, date DATE, day TEXT, time TIME, description TEXT, priority TEXT, status TEXT)')
 
def data_entry():
    date = '2019-02-21'
    day = convert_date_to_day(date)
    c.execute("INSERT INTO tasks VALUES(4, 'Graduate', ?, ?, '10:15:00', 'Graduation ceremony', 'low', 'incomplete')",(date, day))
    conn.commit() 
    c.close() 
    conn.close() 
    
def convert_date_to_day(date):
    year, month, day = (int(x) for x in date.split('-'))
    answer = datetime.date(year, month, day).weekday()
    day = calendar.day_name[answer]
    return day
    
def dynamic_data_entry(title, date, time, priority, description):
    c.execute('INSERT INTO tasks(title, date, day, time, priority, description) VALUES (?, ?, ?, ?, ?)', (title, date, time, priority, description))
    conn.commit()
    
def getdb():
   conn=sqlite3.connect(db_path)
   c=conn.cursor()
   return (c,conn)

def retrieve_data():
   c,conn=getdb()
   c.execute('SELECT * FROM tasks')
   response=c.fetchall()
   data={'tasks':[]}
   for row in response:
       data['tasks'].append({'id':row[0],'title':row[1],'date':row[2],'time':row[3],'description':row[4],'status':row[5]})
   data = json.dumps(data)
   data = json.loads(data)
   return data

def retrieve_data_seventeen_feb():
   c,conn=getdb()
   c.execute('''SELECT * 
             FROM tasks
             WHERE date = '2019-02-17'
             ''')
   response=c.fetchall()
   data={'tasks':[]}
   for row in response:
       data['tasks'].append({'id':row[0],'title':row[1],'date':row[2],'time':row[3],'description':row[4],'status':row[5]})
   data = json.dumps(data)
   data = json.loads(data)
   print(data)
   return data

def retrieve_data_eighteen_feb():
   c,conn=getdb()
   c.execute('''SELECT * 
             FROM tasks
             WHERE date = '2019-02-18'
             ''')
   response=c.fetchall()
   data={'tasks':[]}
   for row in response:
       data['tasks'].append({'id':row[0],'title':row[1],'date':row[2],'time':row[3],'description':row[4],'status':row[5]})
   data = json.dumps(data)
   data = json.loads(data)
   print(data)
   return data
    
#data_entry()
  
#date = '2019-02-20'
#year, month, day = (int(x) for x in date.split('-'))
#answer = datetime.date(year, month, day).weekday()
#date = calendar.day_name[answer]
#print(date)
    
data_entry()
    
    
    
    
    