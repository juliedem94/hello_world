# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:39:32 2017

@author: РС
"""

import helpers



region= 'D:/Anacona & Github/код/hello_world/data moskovskij/'
school_indexes=helpers.jsonLoad(region + 'moskovskij.json')
universities_rates = helpers.loadXLSX('D:/Anacona & Github/код/hello_world/uni','ВК Имена')
schools=helpers.jsonLoad('D:/Anacona & Github/код/hello_world/data/schools.json')

def uni_school_plot(region, number):
    school_mean=[]
    uni_mean=[]
    school_id=[]
    
    for school_index in school_indexes:
        
        #get uni_mean
        print('--------------------School ' + str(school_index['School']) + '----------------------------')
        universities_list=helpers.jsonLoad(region + 'uni_school_' + str(school_index['School']) + '.json')
        
        summ=0
        qty=0
        
        
        for student in universities_list.keys():
            curr_university = universities_list.get(student)
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
        
            school_mean.append(float(school_index['Rate']))
            
            school_dict=schools.get(str(school_index['School']))
            school_name=school_dict.get("name")
            school_id.append(str(school_name) + '('+ str(qty) + ')')
                    
          
    print(school_mean)
    print(uni_mean)
    print(school_id)
    
    #correlation and graph
       
    from scipy import stats
    print ('--------------------------corr------------------------------')
    print(stats.pearsonr(uni_mean, school_mean))
    
    #строим график
    import matplotlib.pyplot as plt
    plt.figure(figsize=(25,25))
    plt.plot(range(5))
    plt.ylim(30,100)
    plt.xlim(30,100)
    plt.xlabel('university')
    plt.ylabel('school')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.scatter(uni_mean, school_mean)
    for i, txt in enumerate(school_id):
        plt.annotate(txt, (uni_mean [i],school_mean [i]))
    plt.savefig(region + 'moskovskij_corr_1.pdf')
