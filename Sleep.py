# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import pickle, time
from datetime import datetime
import tzlocal

temporary_dict={}


#a=[0,5] 
data = pickle.load(open('C:/код/poststime1993.p', 'rb'))
for user in data:
    value = data[user]
    temporary=[] # список часов написания постов. обновляется для каждого пользователя
    #print(value)
    for a in value:
        print(user)
        print(a)
        print('-----CHANGING TIME-------')
        local_timezone = tzlocal.get_localzone() # get pytz timezone
        local_time = datetime.fromtimestamp(a, local_timezone)
        z=local_time.strftime("%H")
        print(z)
        print('==============================================')
        temporary.append(int(z))
        
    print(temporary)
    temp_length=len(temporary) 
    for i in temporary:
        print(i)
        break
        '''ii=0
        if i==i+1:
            ii+=1
        else:
            continue
        quot=ii/temp_length
        print(i)
        print(quot)
#словарь час:доля постов в этот час             
        temporary_dict[i] = quot
    break
print(temporary_dict)'''

    
        
        
        
        
        
        
        
'''spbtime = time.localtime(a)
        print(spbtime)
        print('===========================================')
        break'''









    
'''b = time_dict.get([a])
    print (b)'''
    #print(b) # 'dict' object cannot be interpreted as an integer
'''for c in b: ##один из списка значений ключа а
       
        local_timezone = tzlocal.get_localzone() # get pytz timezone
        local_time = datetime.fromtimestamp(c, local_timezone)
        print(local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))
        break'''