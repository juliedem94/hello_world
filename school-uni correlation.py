# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:39:32 2017

@author: РС
"""

import vk, math, time, helpers

token = 'e7f074457244c512f745a3bfbe1792179e1eb63871ae8da751d77a57c1f32f5e5b137a265dac7247ee9cd'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

school_indexes=helpers.jsonLoad('D:/Anacona & Github/код/hello_world/towns/centralnyj.json')
universities_rates = helpers.loadXLSX('D:/Anacona & Github/код/hello_world/uni','ВК Имена')

school_mean=[]
uni_mean=[]

for school_index in school_indexes:
    
    #get uni_mean
    print('--------------------School ' + str(school_index['School']) + '----------------------------')
    universities_list=helpers.jsonLoad('D:/Anacona & Github/код/hello_world/data centralnyj/uni_school_' + str(school_index['School']) + '.json')
    
    summ=0
    qty=0
    
    for curr_university in universities_list.values():
       #print(curr_university)
    
       for curr_rate in universities_rates:
            if curr_rate['Name']==curr_university:
                if curr_rate['Rate'] !=None:
            
                    qty+=1
                    summ+=curr_rate['Rate']
                       
    
    if qty !=0: 
        mean = summ/qty
        uni_mean.append(mean)
        print(mean)
    
        curr_school_uni_qty=0
        for a in universities_list: 
            curr_school_uni_qty+=1
        
        if curr_school_uni_qty > 0:
            school_rate=school_index['Rate']
            school_mean.append(float(school_rate))
        
        #print(curr_school_uni_qty)        
        
print(school_mean)
print(uni_mean)
    
#correlation and graph

from scipy import stats
print ('--------------------------corr------------------------------')
print(stats.pearsonr(uni_mean, school_mean))

#строим график
import matplotlib.pyplot as plt
plt.scatter(uni_mean, school_mean)
plt.savefig('D:/Anacona & Github/код/hello_world/data centralnyj/uni-school corr 1.pdf')
