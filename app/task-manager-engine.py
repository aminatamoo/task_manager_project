# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:47:47 2019

@author: ottil
"""

import sqlite3
import json 

conn = sqlite3.connect('tasks.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasks (id REAL, title TEXT, date DATE, time TIME, description TEXT, priority TEXT, status TEXT)')
 
def data_entry():
    c.execute("INSERT INTO tasks VALUES(2, 'Clean', '2019-01-22', '11:30:00', 'Clean room and do laundry', 'medium', 'incomplete')")
    conn.commit() 
    c.close() 
    conn.close() 

