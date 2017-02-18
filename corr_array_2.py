# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:42:21 2017

@author: РС
"""

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
            
#-------------------------------CHANGES-----------------------------------------#  
            if n==0:           
                school_mean_overall.append(float(school_index['Rate']))
                uni_mean_overall.append(mean)
                school_id_overall.append(str(school_name) + '('+ str(qty) + ')')
#-------------------------------CHANGES-----------------------------------------#
           


    if len(uni_mean) <= 1:
        return ('out of students')
    else: 
        #строим график
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
corr_list_overall = []
n_list_overall = []


    
   
school_mean_overall=[]    
uni_mean_overall=[]
school_id_overall=[]


for curr_reg in regions:
    corr_list = []
    n_list = []
    for n in range(100):
        res = plot(root,curr_reg, n)
        if res != 'out of students':
            corr_list.append(res[0]) 
            n_list.append(n)
        
    #print(corr_list)
    #print(n_list)

    #строим график корреляций по району
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.rc('font', family='Arial')
    plt.figure(figsize=(25,25))
    plt.xlabel('N')
    plt.ylabel('Correlation')
    plt.plot(n_list,corr_list)
    plt.savefig(root + 'data ' + curr_reg + '/corr.by N' + '.pdf')
    #----------------------------------------------------------------------
          
    
if len(uni_mean_overall) > 1:
        
    #строим график скаттер по всем районам
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
    plt.savefig(root + '/corr.overall.scatter.N=0'+'.pdf')
    #-----------------------------------------------------------------------

    for n_overall in range(50):

        corr_list_overall.append(stats.pearsonr(uni_mean_overall, school_mean_overall)[0])
        n_list_overall.append(n_overall)
    

#строим график корреляций по N по всем районам
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        mpl.rc('font', family='Arial')
        plt.figure(figsize=(25,25))
        plt.xlabel('N')
        plt.ylabel('Correlation')
        plt.plot(n_list_overall,corr_list_overall)
        plt.savefig(root + '/corr.by N overall' + '.pdf')
        #----------------------------------------------------------------------































