#%%
import helpers, vk, time

#%% Загружаем школы нашего района
schools = helpers.jsonLoad('data/moskovskij.json')

#%%
token = '746f1fbb79cf26e44dad6ffc19aa2128ff781583998ad806d23a7be84b72c928e96affa9d37c93d10a427'
session = vk.Session(access_token = token) 
api = vk.API(session, v = '5.45')

#%%
for school in schools:
    
    print('----------------------School ', school['School'], '----------------------------------')
    time.sleep(1)
    vk_data = api.users.search(school = school['School'], count=1000, birth_year = 1996)
    users = vk_data['items']
    result = []
    for curr_user in users:
        result.append(curr_user['id'])
    file_name = 'data/users_' + str(school['School']) + '.json'
    helpers.jsonSave(file_name, result)