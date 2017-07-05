

import pickle
from datetime import datetime
import tzlocal
from collections import Counter
from matplotlib import pyplot as plt

common_dict={}
common=[]
common2=[]

data = pickle.load(open('D:/код/hello_world/Sleep/poststime1993.p', 'rb'))


for user in data:
    value = data[user]
    user_save='D:/код/hello_world/Sleep/'
    temporary=[]# список часов написания постов. обновляется для каждого пользователя
    temporary_dict=[]
    
    if len(value) >= 10000:
        
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
    else:
        print('NOT ENOUGH POSTS')
        continue;
    print(temporary)
           
    temp_length=len(temporary) 
    print(temp_length)
    count=Counter(temporary)
    for i in range(0, 24):
        temporary_dict.append(count[i] / temp_length)
    print(temporary_dict)
    common.append(temporary_dict)
    plt.plot(temporary_dict)
    #plt.savefig(user_save + 'publish-hour-' + str(user) + '.pdf')
    plt.gcf().clear()
    
bbb=0
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print(common)
common_length=len(common)

for ii in range(0,24):
    bb=0
    for b in common:
        bb+=b[ii]
        final=bb/common_length
    common2.append(final)


print('.........................................')
print(common2)
    
plt.plot(common2)
plt.savefig('D:/код/hello_world/Sleep/true-publish-hour-all 10 000' + '.pdf')
     
    
    
    
    
