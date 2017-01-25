# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:15:03 2017

@author: РС
"""

import vk, math, time, pickle, helpers

token = 'dc8f832ac59fe7e40088dec5ed0a3eb3ed314797f27b22d89f8bc123d4f660afdb03f86be24a0afa87635'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

def get_friends(users):
    data = []
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
                done = True
            except:                
                error_count += 1
                print("Error!")
                time.sleep(1)
                if error_count > 5:
                    print('Too many errors in a row :(')
                    done = True
            
        data = data + sub_data
        print(i + 1, 'out of', max_num)
            
    return data    
   
school_index = helpers.jsonLoad('data/moskovskij.json')   
    
h=0
curr_school = 0

while h<34:
    
    print('----------------------School '+str(school_index[h]['School'])+'----------------------------------')
    
    curr_school=school_index[h]['School']
    
    users_id=pickle.load(open('C:/Users/РС/Desktop/код/hello_world/data/' + str(curr_school) + '.p', "rb" ))
    
    users_friends_sum =[] 
   
    users_friends_sum = get_friends(users_id)
    
    
    helpers.jsonSave('C:/Users/РС/Desktop/код/hello_world/data/friends_school_' + str(curr_school), users_friends_sum)                                             
    h=h+1
    print('------------------done-------------------')




