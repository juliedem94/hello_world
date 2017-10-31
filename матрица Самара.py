# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:20:18 2017

@author: Julia
"""

import helpers
total_dict={}
qq=[]

school_indexes = helpers.jsonLoad('D:/код/hello_world/Самара сеть дружбы школ/schools_full.json')
all_users=helpers.jsonLoad('D:/код/hello_world/Самара сеть дружбы школ/student-school.json')

for v in school_indexes:
    school_index=str(v['vk_id'])
    qq.append(school_index) # qq - список айди всех школ
    
for q in qq:
    
    fr_list=[]
    friends=[]
    a=helpers.jsonLoad('D:/код/hello_world/Самара сеть дружбы школ/friends_school_' + q + '.json')
    for human in a:
        friendss=a.get(human)
        fr_list.append(friendss)
    for lst in fr_list:
        if lst != None:
            for el in lst:
                friends.append(el) #friends - список всех друзей всех пользователей этой школы
    
    total_list=[]   
    for friend in friends: # ищу айди одного друга в словаре всех пользователей Самары и их школ
        for ab in all_users:
            if friend==ab:
                if all_users.get(friend)!= None:
                    print(ab)
            '''total_list.append(all_users.get(friend))
            print(total_list)

            total_dict[q]=total_list
helpers.jsonSave('D:/код/hello_world/Самара сеть дружбы школ/school-friends`schools.json', total_dict)
            
# матрица пользователей и групп
x=len(school_ids)
y=len(school_ids)
matrix = np.zeros((x,y), dtype=np.int)

icount = 0
for i in school_ids:
    qcount = 0
    for q in groups_100:
        
        gr=i.get('groups')
        
        if q in gr:
            matrix[icount,qcount] = 1
        qcount+=1
    icount+=1
 

df = pd.DataFrame(matrix, index=users_100_ids, columns=groups_100)
df.to_csv('df.csv', index=True, header=True, sep=';')'''                
    
    
    
    



