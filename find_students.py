# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:15:03 2017

@author: РС
"""

import vk
import time
import helpers


token = 'a564bbc9a25bb90f00991f7ca27b135c7809326e2cd9165174ea114f96e3b216a80e0862b3ef419372fcb'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

region='C:/код/hello_world/data petrogradskij/'
file_name='petrogradskij.json'

school_indexes = helpers.jsonLoad(region + file_name)


for school_index in school_indexes:
    
    print('----------------------School '+ str(school_index['School'])+'----------------------------------')

    vk_data = api.users.search(school = school_index['School'], count=1000, birth_year = 1996)
    users = vk_data['items'] 
    time.sleep(0.35)
    
    
    users_id = [s['id'] for s in users]
    #print(users_id)
    
    helpers.jsonSave(region + str(school_index['School']) +'.json', users_id)
   
    












