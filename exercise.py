# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:19:25 2017

@author: РС
"""

import helpers
from collections import Counter
import numpy as np
import pandas as pd

users_groups=helpers.jsonLoad('D:/код/hello_world/упражнение/groups.json')

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

#сделали матрицу пользователей и групп
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

#print(np.sum(matrix))

# матрица пола пользователей
users_sex=helpers.jsonLoad('D:/код/hello_world/упражнение/info.json')
z_dict={}
for z in users_sex:
    z_sex= z.get('sex')
    z_id=z.get('id')
    z_dict[str(z_id)]=str(z_sex)
#print(hhh)

x=len(users_100)
y=1
matrix2 = np.zeros((x,y), dtype=np.int)

ccount = 0
for c in users_100_ids:
    d=z_dict.get(c)    
    matrix2[ccount,0] = d
    ccount+=1
 

df2 = pd.DataFrame(matrix2, index=users_100_ids)
df2.to_csv('df2.csv', index=True, header=True, sep=';')

#print(matrix2)
#Regression
from sklearn import linear_model
count = 0
n_list1=[]
reg_list1=[]
regr_dict1={}

n_list2=[]
reg_list2=[]
regr_dict2={}

from sklearn.decomposition import PCA
pca = PCA(n_components = min(matrix.shape))
M_pca = pca.fit_transform(matrix)

for ii in range(1,500):
    
    X1=M_pca[0:548, 0:ii]
    y1=matrix2[0:548,:]
    X2=M_pca[548:, 0:ii]
    y2=matrix2[548:,:]
    regr = linear_model.LogisticRegression()
    regr.fit(X1,y1.ravel())

    print('=========================================================')
    #print(ii)
    #print(users_100_ids[ii])
    #11111print(matrix2[ii,0])
    print(count)
    print(regr.score(X1,y1))
    print(regr.score(X2,y2))
    
    n_list1.append(ii)
    reg_list1.append(regr.score(X1,y1))  
    n_list2.append(ii)
    reg_list2.append(regr.score(X2,y2))  

    regr_dict1[int(count)]=float(regr.score(X1,y1))
    regr_dict2[int(count)]=float(regr.score(X2,y2))

    count+=1
print(regr.predict(X1))
print(regr.predict(X2))

#print(regr_dict)
helpers.jsonSave('D:/код/hello_world/regression1.json', regr_dict1)
helpers.jsonSave('D:/код/hello_world/regression2.json', regr_dict2)
  
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('font', family='Arial')
#plt.figure(figsize=(25,25))
plt.xlabel('N')
plt.ylabel('Regression')
plt.ylim(0.6,1.2)
plt.xlim(0,500)
plt.plot(n_list1,reg_list1)
plt.savefig('D:/код/hello_world/Regression_groops_sex3.pdf')

plt.plot(n_list2,reg_list2)
plt.savefig('D:/код/hello_world/Regression_groops_sex4.pdf')
    

































