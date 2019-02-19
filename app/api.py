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
        
    

    
