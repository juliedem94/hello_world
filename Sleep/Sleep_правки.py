# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:19:11 2017

@author: Julia
"""
i=0
i+=1
#if i == 5:
#break;

#%%

import helpers
from collections import Counter
from matplotlib import pyplot as plt

user_save='D:/код/hello_world/Sleep/'

common_dict={}
common=[]
common2=[]

data = helpers.jsonLoad('D:/код/hello_world/Sleep/Poststime93new.json')


for user in data:        
    temporary = data[user]# список часов написания постов для каждого юзера   
    temporary_list=[] #список долей часов          
    temp_length=len(temporary)
    
    if temp_length>=50000:

        count=Counter(temporary)
        for i in range(0, 24):
            temporary_list.append(count[i] / temp_length)
        common.append(temporary_list)
        #plt.plot(temporary_list)
        #plt.savefig(user_save + 'publish-hour-' + str(user) + '.pdf')
        #plt.gcf().clear()
    else:
        continue;
    
print(common)
common_length=len(common)

for ii in range(0,24):
    bb=0
    for b in common:
        bb+=b[ii]
    final=bb/common_length
    common2.append(final)
    
result = []
labels = []
for i in range(0, 24):
    ii = i + 6
    if ii > 23: ii = ii - 24
    result.append(common2[ii])
    labels.append(ii)    
    
    
plt.plot(result)
plt.xticks(range(0, 24), labels)
plt.savefig('D:/код/hello_world/Sleep/publish-hour-new 50 000' + '.pdf')
        
    
    
    
