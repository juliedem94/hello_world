# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:15:03 2017

@author: РС
"""

import vk
import time
import helpers


token = 'e7f074457244c512f745a3bfbe1792179e1eb63871ae8da751d77a57c1f32f5e5b137a265dac7247ee9cd'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')


school_indexes = helpers.jsonLoad('D:/Anacona & Github/код/hello_world/towns/centralnyj.json')


for school_index in school_indexes:
    
    print('----------------------School '+ str(school_index['School'])+'----------------------------------')

    vk_data = api.users.search(school = school_index['School'], count=1000, birth_year = 1996)
    users = vk_data['items'] 
    time.sleep(0.35)
    
    
    users_id = [s['id'] for s in users]
    #print(users_id)
    
    helpers.jsonSave('D:/Anacona & Github/код/hello_world/data centralnyj/' + str(school_index['School']) +'.json', users_id)
   
    












