# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:15:03 2017

@author: РС
"""

import vk, math, time, pickle, helpers

token = '602a5062a5050238895c95c78144a3d68303ebe23d0b6ea64c96fcb913009cd035e3707e1f960f307fc2f'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

def get_friends(users):
    data = {}
    max_num = math.floor(len(users) / 20) + 1
    for i in range(0, max_num):
        new_users = users[i * 20:i * 20 + 20]
        sub_data = []
        code_parts = []
        for user in new_users:
            code_parts.append('API.friends.get({"user_id": ' + str(user)+'}).items')
        code_string = 'return [' + ','.join(code_parts) +'];'  
        print(code_string)
        done = False
        error_count = 0
        while not done:
            try:
                time.sleep(0.335)   
                sub_data = api.execute(code = code_string, timeout = 60)
                
                dict_out = {}

                for x, y in zip(new_users, sub_data):
                    dict_out[x] = y
                
                
                
                done = True
            except:                
                error_count += 1
                print("Error!")
                time.sleep(1)
                if error_count > 5:
                    print('Too many errors in a row :(')
                    done = True
            
        data.update(dict_out)
        print(i + 1, 'out of', max_num)
            
    return data    
   
school_indexes = helpers.jsonLoad('data/moskovskij.json')   
    

curr_school = 0

for school_index in school_indexes:
      
    print('----------------------School '+str(school_index['School'])+'----------------------------------')
    
    users_ids=pickle.load(open('/код/hello_world/data/' + str(school_index['School']) + '.p', "rb" ))
    
    users_friends_sum =[] 
   
    users_friends_sum = get_friends(users_ids)
    print(users_friends_sum)
    
    helpers.jsonSave('/код/hello_world/data/friends_school_' + str(school_index['School']), users_friends_sum)                                             

print('------------------done-------------------')
    



