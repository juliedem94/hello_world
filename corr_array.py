# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:43:36 2017

@author: РС
"""

import helpers

def uni_array(region):
    school_indexes=helpers.jsonLoad(region + file_name)
    universities_rates = helpers.loadXLSX('C:/код/hello_world/uni','ВК Имена')
    schools=helpers.jsonLoad('C:/код/hello_world/data/schools.json')
    
    
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
                           
        
        if qty >n: 
            mean = summ/qty
            unis_array.append(mean)
            print(mean)
        
            #school_mean.append(float(school_index['Rate']))
            
            school_dict=schools.get(str(school_index['School']))
            school_name=school_dict.get("name")
            school_id.append(str(school_name) + '('+ str(qty) + ')')
            
def school_array(region):
    school_indexes=helpers.jsonLoad(region + file_name)
    universities_rates = helpers.loadXLSX('C:/код/hello_world/uni','ВК Имена')
    schools=helpers.jsonLoad('C:/код/hello_world/data/schools.json')
    
    
    
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
                           
        
        if qty >n: 
            #mean = summ/qty
            #uni_mean.append(mean)
        
            schools_array.append(float(school_index['Rate']))
            
            school_dict=schools.get(str(school_index['School']))
            school_name=school_dict.get("name")
            school_id.append(str(school_name) + '('+ str(qty) + ')')       
      
schools_array=[]
unis_array=[]

n=0

region='C:/код/hello_world/data moskovskij/'
file_name='moskovskij.json'  
    
schools_array.append(school_array(region))    
unis_array.append(uni_array(region))    
    
print(schools_array)   
print(unis_array)   


















