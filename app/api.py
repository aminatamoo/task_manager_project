# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:14:58 2019

@author: amina
"""

import json
import sqlite3

db_path ='static/tasks.db'

def getdb():
    conn=sqlite3.connect(db_path)
    c=conn.cursor()
    return (c,conn)

def create_table():
    c,conn=getdb()
    c.execute('CREATE TABLE IF NOT EXISTS tasks (id REAL, title TEXT, date DATE, time TIME, description TEXT, priority TEXT, status TEXT)')
 
def data_entry(id_t,title,date,time,description,priority,status):
    c,conn=getdb()
    c.execute("INSERT INTO tasks VALUES(?,?,?,?,?,?,?)",(id_t,title,date,time,description,priority,status))
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
        
    

    

