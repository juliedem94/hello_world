# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:39:32 2017

@author: РС
"""

import vk, math, time, helpers

token = 'f0b2643a646170120fdf9e259e222783fbf99f069aedbeeb31dcaab5a53a504a3ee0b60b195f633b158fc'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

school_indexes=helpers.jsonLoad('/код/hello_world/data/moskovskij.json')
universities_rates = helpers.loadXLSX('/код/hello_world/data/uni','ВК Имена')

school_mean=[]
uni_mean=[]

for school_index in school_indexes:
    
    #get school_mean
    school_rate=school_index['Rate']
    school_mean.append(float(school_rate))
    #print(school_rate)
    
    #get uni_mean
    print('--------------------School ' + str(school_index['School']) + '----------------------------')
    universities_list=helpers.jsonLoad('/код/hello_world/data/uni_school_' + str(school_index['School']) + '.json')
    
    summ=0
    qty=0
    
    for curr_university in universities_list.values():
        #print(curr_university)
        for curr_rate in universities_rates:
            if curr_rate['Name']==curr_university:
                #if curr_rate['Rate'] !=None:
            
                    qty+=1
                    summ+=curr_rate['Rate']

    if qty !=0: 
        mean = summ/qty
        uni_mean.append(mean)
        print(mean)
    else:
        print(0)
        uni_mean.append(0)
print(school_mean)
print(uni_mean)
    
#correlation and graph

from scipy import stats
print ('--------------------------corr------------------------------')
print(stats.pearsonr(uni_mean, school_mean))

#строим график
import matplotlib.pyplot as plt
plt.scatter(uni_mean, school_mean)

