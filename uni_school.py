# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:49:47 2017

@author: РС
"""
import vk, math, time, helpers

token = '78bc126e0670dacedcc062b905bd83b5e275a5c9e760c60029fc5a4291c9b3c5f2b2f63f0930760b8ad6c'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

school_indexes = helpers.jsonLoad('/код/hello_world/data/moskovskij.json')  

#шаг 1: загрузить айди учеников школ и посмотреть есть ли хоть один из них в друзьях друг у друга
for school_index in school_indexes:
    print('----------------------School '+str(school_index['School'])+'----------------------------------')
    users_and_friends = helpers.jsonLoad('/код/hello_world/data/friends_school_' + str(school_index['School']) + '.json') 

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
                    
                    
    helpers.jsonSave('/код/hello_world/data/uni_school_' + str(school_index['School']) + '.json', curr_school_unis)                                             
    print('---------------DONE--------------------')
   
     































