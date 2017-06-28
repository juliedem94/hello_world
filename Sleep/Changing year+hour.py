# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 00:47:52 2017

@author: Julia
"""


import pickle, helpers
from datetime import datetime
import tzlocal
from collections import Counter
from matplotlib import pyplot as plt

data = pickle.load(open('D:/код/hello_world/Sleep/poststime1993.p', 'rb'))
users_by_years={}

i=0
for user in data:
    new_time={}
    value = data[user]         
    for a in value:
        local_timezone = tzlocal.get_localzone() # get pytz timezone
        local_time = datetime.fromtimestamp(a, local_timezone)
        z=local_time.strftime("%Y-%m-%d %H:%M:%S")
        
        if new_time.get(z[0:4])==None:
            curr_posts = []
            curr_posts.append(int(z[11:13]))
            new_time[z[0:4]]=curr_posts
        else:
            curr_posts = new_time[z[0:4]]
            curr_posts.append(int(z[11:13]))
            new_time[z[0:4]]=curr_posts
                    
    users_by_years[user]=new_time    
               
    i+=1
    if i==100:
        break;    
    

#print(users_by_years)


common={}

for user in users_by_years: 
    
    temporary = users_by_years[user]# список часов написания постов для каждого юзера 
    curr_user_parts = {}
                              
    for year in temporary:        
       
        temporary_list=[] #список долей часов          
        temp_length=len(temporary[year])
        
        #if temp_length>=50000:
    
        count=Counter(temporary[year])
        for i in range(0, 24):
            temporary_list.append(count[i] / temp_length)
        
        curr_user_parts[year] = temporary_list
        
    common[user] = curr_user_parts          
            
    
#print(common)

posts_by_years = {}

for user in common: 
    
    temp = common[user]

    for year in temp:
        
        if posts_by_years.get(year)==None:
            
            curr_year = temp[year]
            curr_year.append(1)
            posts_by_years[year] = curr_year
        
        else:    
            
            
            curr_year = posts_by_years[year]
            new_year = []
            
            for ii in range(0,24):
                new_year.append(curr_year[ii]+temp[year][ii])
            new_year.append(curr_year[24]+1)
            
            posts_by_years[year] = new_year
            
#print(posts_by_years)            

common_length=len(common)

for year in posts_by_years:
    print(year)
    common2 = []
    curr_year = posts_by_years[year]
    for ii in range(0,24):
        common2.append(curr_year[ii]/curr_year[24])
    
    result = []
    labels = []
    for i in range(0, 24):
        ii = i + 6
        if ii > 23: ii = ii - 24
        result.append(common2[ii])
        labels.append(ii)    
    
    
    plt.plot(result)
    plt.xticks(range(0, 24), labels)
    plt.show()
    plt.savefig('D:/код/hello_world/Sleep/publish-hour-by-year-' + year + '.pdf')
    plt.gcf().clear()
    
#helpers.jsonSave('D:/код/hello_world/Sleep/Poststimeyear.json',temporary) 