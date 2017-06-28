# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:26:49 2017

@author: Julia
"""

import pickle, helpers
from datetime import datetime
import tzlocal

data = pickle.load(open('D:/код/hello_world/Sleep/poststime1993.p', 'rb'))
temporary={}

i=0
for user in data:
    new_time=[]
    value = data[user]         
    for a in value:
        local_timezone = tzlocal.get_localzone() # get pytz timezone
        local_time = datetime.fromtimestamp(a, local_timezone)
        z=local_time.strftime("%H")
        new_time.append(int(z))
    temporary[user]=new_time
    print(temporary)

    i+=1
    if i==5:
        break;
helpers.jsonSave('D:/код/hello_world/Sleep/Poststimenew.json',temporary) 