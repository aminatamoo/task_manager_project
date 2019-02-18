# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:14:58 2019

@author: amina
"""

import json

data={'tasks':[{'id':1,'title':'homework', 'date':'22/03/2019','time':'12:00',  'description':'Complete trigonometry assignment for AM1001 Module','priority':'high','status':'complete'},{'id':2, 'title':'shopping', 'date':'24/03/2019','time':'10:00',  'description':'Get potatoes and chicken from the supermarket','priority':'low','status':'incomplere'},{'id':3, 'title':'cleaning', 'date':'27/03/2019','time':'13:00',  'description':'Clean the bathroom and kitchen','priority':'medium','status':'incomplete'}]}

data_json=json.dump(data)