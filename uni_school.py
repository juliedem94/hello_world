# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:49:47 2017

@author: РС
"""
import vk,  time, helpers

token = 'a564bbc9a25bb90f00991f7ca27b135c7809326e2cd9165174ea114f96e3b216a80e0862b3ef419372fcb'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

region='C:/код/hello_world/data petrogradskij/'
file_name='petrogradskij.json'

school_indexes = helpers.jsonLoad(region+file_name)  

#шаг 1: загрузить айди учеников школ и посмотреть есть ли хоть один из них в друзьях друг у друга
for school_index in school_indexes:
    print('----------------------School '+str(school_index['School'])+'----------------------------------')
    users_and_friends = helpers.jsonLoad(region + 'friends_school_' + str(school_index['School']) + '.json') 

    true_users=[]

    for curr_user in users_and_friends:
        
        curr_user_friends = users_and_friends.get(curr_user)
      
        if curr_user_friends != None:

            for friend in curr_user_friends:
                
             
                
                if users_and_friends.get(str(friend)) != None:
                    true_users.append(curr_user)
                   
                    break
                
                
    curr_school_unis={}

    true_users_string = ','.join(true_users)
    time.sleep(0.335)
    user_uni = api.users.get(user_ids = (true_users_string), fields = 'universities')            
    
    for j in range(len(user_uni)):
        curr_user_uni_list = user_uni[j]
        curr_user_id=curr_user_uni_list.get('id')
        uni_info_list = curr_user_uni_list.get('universities')
            
        if uni_info_list !=None:
            for k in range(len(uni_info_list)): 
                curr_school_unis[curr_user_id]=uni_info_list[k]['name']
                    
                    
    helpers.jsonSave(region + 'uni_school_' + str(school_index['School']) + '.json', curr_school_unis)                                             
    print('---------------DONE--------------------')
   
     































