# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:19:25 2017

@author: РС
"""

import helpers
from collections import Counter
import numpy as np
import pandas as pd

users_groups=helpers.jsonLoad('C:/код/hello_world/упражнение/groups.json')

# 1 микро шаг - делаем спсиок уникальных группп и считаем их количество
g_list=[]

for a in users_groups:
    group_lists=a.get('groups')
    #print(group_lists)
    for group in group_lists:
        g_list.append(group) # g_list - список всех групп с повторами
uniq_groups=dict(zip(g_list,g_list)).values()
#print (uniq_groups)
#print(len(uniq_groups))

# 2 микро шаг - посчитать группы, на которые подписано больше 100 человека.
groups_100=[]
n=0
count_groups=Counter(g_list) #словарь id группы: число  подписчиков из дата-сета
#print (count_groups)
for k in count_groups:
    if count_groups.get(k) >= 100:
        groups_100.append(k)
        n+=1
#print(groups_100)
# 3 микро шаг. набрать пользователей, кот подписаны на больше чем 100 групп
users_100=[]
users_100_ids=[]
l=0
#print(groups_100)
#print(len(groups_100))
for j in users_groups:
    gr=j.get('groups')
    
    if (len(gr)) >= 100:
        counter = 0
        for g in range(len(gr)):
            
            if gr[g] in groups_100:
                counter+=1
            
              
        if counter>=100:
            print(j.get('id') + '-----------------------')
            print(counter)  
            users_100_ids.append(j.get('id'))
            users_100.append(j)
            
#print(users_100)
#print(len(users_100))


x=len(users_100)
y=len(groups_100)
matrix = np.zeros((x,y), dtype=np.int)

icount = 0
for i in users_100:
    qcount = 0
    for q in groups_100:
        
        gr=i.get('groups')
        
        if q in gr:
            matrix[icount,qcount] = 1
        qcount+=1
    icount+=1
 

df = pd.DataFrame(matrix, index=users_100_ids, columns=groups_100)
df.to_csv('df.csv', index=True, header=True, sep=';')

print(np.sum(matrix))
