# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:43:36 2017

@author: РС
"""

import helpers
from scipy import stats
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:39:32 2017

@author: РС
"""



def plot(root_dir,region, n):
    school_indexes=helpers.jsonLoad(root_dir + 'data '+ region + "/" + region + '.json')
    universities_rates = helpers.loadXLSX(root_dir + 'uni','ВК Имена')
    schools=helpers.jsonLoad(root_dir + 'data/schools.json')
    
    
    school_mean=[]
    uni_mean=[]
    school_id=[]
    
    for school_index in school_indexes:
        
        #get uni_mean
        print('--------------------School ' + str(school_index['School']) + '----------------------------')
        universities_list=helpers.jsonLoad(root_dir + 'data ' + region + '/uni_school_' + str(school_index['School']) + '.json')
        
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
                           
        
        if qty > n: 
            mean = summ/qty
            uni_mean.append(mean)
            print(mean)
        
            school_mean.append(float(school_index['Rate']))
            
            school_dict=schools.get(str(school_index['School']))
            school_name=school_dict.get("name")
            school_id.append(str(school_name) + '('+ str(qty) + ')')
            
            


    if len(uni_mean) <= 1:
        return ('out of students')
    else: 
        
        global curr_overall
        curr_overall = {}
        curr_overall['uni_mean'] = uni_mean
        curr_overall['school_mean'] = school_mean
        curr_overall['school_id'] = school_id

            
        
        #строим график scatter для каждого района
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        mpl.rc('font', family='Arial')
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
        plt.savefig(root_dir + 'data ' + region + '/corr.N=' + str(n) + '.pdf')
        
        
        return stats.pearsonr(uni_mean, school_mean)
        
#-------------------------------конец--функции---------------------------------------   


regions=[]

regions.append('moskovskij')
regions.append('admiraltejskij')
regions.append('centralnyj')
regions.append('frunzenskij')
regions.append('kalininskij')
regions.append('kirovskij')
regions.append('kolpinskij')
regions.append('krasnogvardejskij')
regions.append('krasnoselskij')
regions.append('kronshtadtskij')
regions.append('kurortnyj')
regions.append('nevskij')
regions.append('petrodvorzovyj')
regions.append('petrogradskij')
regions.append('primorskij')
regions.append('pushkinskij')
regions.append('vasileostrovskij')
regions.append('vyborgskij')

root = 'C:/код/hello_world/'

curr_overall = {}
dict_overall = {}



for curr_reg in regions:
    
    corr_list = []
    n_list = []
    curr_reg_dict = {}
    
    for n in range(100):
        
        res = plot(root,curr_reg, n)
        if res != 'out of students':
            n_list.append(n)
            corr_list.append(res[0])
            curr_reg_dict[n] = curr_overall
            
        dict_overall[curr_reg] = curr_reg_dict    
            
            

    #строим график корреляций по району для каждого района
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.rc('font', family='Arial')
    plt.figure(figsize=(25,25))
    plt.xlabel('N')
    plt.ylabel('Correlation')
    plt.plot(n_list,corr_list)
    plt.savefig(root + 'data ' + curr_reg + '/corr.by N' + '.pdf')
    #----------------------------------------------------------------------
          
    

''' строим общие графики'''
    

    
for curr_n in range(20):
    
    uni_mean_overall = []
    school_mean_overall = []
    school_id_overall = []
    
    for curr_reg in regions:
    
        curr_reg_data = dict_overall[curr_reg]
        curr_n_data = curr_reg_data.get(curr_n)
        
        if curr_n_data != None:
            
            for el in range(len(curr_n_data['uni_mean'])):
                uni_mean_overall.append(curr_n_data['uni_mean'][el])
                school_mean_overall.append(curr_n_data['school_mean'][el])
                school_id_overall.append(curr_n_data['school_id'][el])

                
    if len(uni_mean_overall) > 0:
        #строим график scatter для всех регионов при curr_n
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        mpl.rc('font', family='Arial')
        plt.figure(figsize=(25,25))
        plt.plot(range(5))
        plt.ylim(30,100)
        plt.xlim(30,100)
        plt.xlabel('university')
        plt.ylabel('school')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.scatter(uni_mean_overall, school_mean_overall)
        for i, txt in enumerate(school_id_overall):
            plt.annotate(txt, (uni_mean_overall [i],school_mean_overall [i]))
        plt.savefig(root + 'corr.overall.N=' + str(curr_n) + '.pdf')    
    
            
 
        
        
n_list_overall = []
corr_list_overall = [] 
        
for n_oa in range(100):
    
    curr_n_school_mean = []
    curr_n_uni_mean = []

    
    for curr_reg in regions:    
        curr_reg_data = dict_overall[curr_reg]
        curr_n_data = curr_reg_data.get(n_oa)
        
        if curr_n_data != None:
            for el in range(len(curr_n_data['uni_mean'])):
                curr_n_uni_mean.append(curr_n_data['uni_mean'][el])
                curr_n_school_mean.append(curr_n_data['school_mean'][el])
                
    if len(curr_n_uni_mean) > 1:
        
        n_list_overall.append(n_oa)
        corr_list_overall.append(stats.pearsonr(curr_n_uni_mean, curr_n_school_mean)[0])
               
        
 #строим график корреляций для всех районов
import matplotlib as mpl
import matplotlib.pyplot as pltoa
mpl.rc('font', family='Arial')
pltoa.figure(figsize=(25,25))
pltoa.xlabel('N')
pltoa.ylabel('Correlation')
pltoa.plot(n_list_overall,corr_list_overall)
pltoa.savefig(root + 'corr.by N' + '.pdf')
#----------------------------------------------------------------------









