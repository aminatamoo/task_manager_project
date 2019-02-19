# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:53:46 2019

@author: ottil
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from task_manager_engine import *

app = Flask("MyApp")
cors = CORS(app)
  
@app.route("/api")
def index():
    data = retrieve_data()
    data_seventeen_feb = retrieve_data_seventeen_feb()
    return render_template("index.html", **locals())

#    if request.method == 'POST':
#        response = request.values
#        return jsonify(response)
#    
#    if request.method == 'GET':
#        methods=['GET','POST']
        

@app.route('/addtask',methods=['GET','POST'])
def get_data():
    if request.method=='POST':
       title=request.form['title']
       date=request.form['date']
       time=request.form['time']
       priority=request.form['priority']
       description=request.form['description']
       dynamic_data_entry(title, date, time, priority, description)
    #   connection = mysql.get_db()
    #   cursor = connection.cursor()
    #   query="INSERT INTO names_tbl(f_name,l_name,e_id) VALUES(%s,%s,%s)"
    #   cursor.execute(query,(first_name,last_name,email_id))
    #   connection.commit()
       return render_template("show_task.html", **locals())


if __name__=='__main__':
    app.run(debug=True)