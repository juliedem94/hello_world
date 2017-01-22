# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:15:03 2017

@author: РС
"""

import vk
import time

from openpyxl import load_workbook
from openpyxl import Workbook



token = '2026881ef3af32890e3f684ef72321d15b722e5c1d6a9dad5a60a272f8e876b438cdb3445356da5e6e1fc'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')


def loadXLSX(name, list_name):
    wb = load_workbook(name + '.xlsx', data_only = True)
    ws = wb[list_name]
    col = 1
    row = 1    
    fields = []
    field = True
    while field:
        field = ws.cell(row = row, column = col).value    
        if field:
            fields.append(field)
            col += 1
    
    data1 = []
    row += 1
    not_empty = True
    while not_empty:
        entry = {}
        not_empty = False
        for i, field in enumerate(fields):
            col = i + 1
            val = ws.cell(row = row, column = col).value            
            entry[field] = val
            if val:
                not_empty = True
        if not_empty:
            data1.append(entry)
            row += 1        
    
    return data1
    
    
school_index = loadXLSX('C:/Users/РС/Desktop/school', 'Лист1')


h=0
curr_school = 0

uni_rate_total=[]
school_rate_total=[]

while h<34:
    
    print('----------------------School '+str(school_index[h]['School'])+'----------------------------------')
    
    curr_school=school_index[h]['School']

    vk_data = api.users.search(school = curr_school,count=1000, birth_year = 1996)
    users = vk_data['items'] 
    time.sleep(0.35)

    wb = Workbook()
    ws = wb['Sheet']
    ws['A1'] = 'UserId'
    
    counter = 2    
    for curr_user in users:
        ws['A'+str(counter)] = curr_user['id'] 
        counter = counter+1  

    wb.save('C:/Users/РС/Desktop/код/hello_world/data/'+ str(curr_school) + '.xlsx')
    
   
    
    
 
    h=h+1  







