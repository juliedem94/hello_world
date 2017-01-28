# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:15:03 2017

@author: РС
"""

import vk
import time
import helpers


token = 'd1419d9d16f7374d62092b30e15eab12ab04a63e31f1d97dc3082e309d1425dbccf63113bd505027ca796'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')


school_indexes = helpers.loadXLSX('/код/hello_world/data/school', 'Лист1')


for school_index in school_indexes:
    
    print('----------------------School '+ str(school_index['School'])+'----------------------------------')

    vk_data = api.users.search(school = school_index['School'], count=1000, birth_year = 1996)
    users = vk_data['items'] 
    time.sleep(0.35)
    
    
    users_id = [s['id'] for s in users]
    #print(users_id)
    
    helpers.jsonSave('/код/hello_world/data/' + str(school_index['School']) +'.json', users_id)
   
    












