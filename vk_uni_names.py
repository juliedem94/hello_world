#%% Получаем список уникальных названий вузов
# Загружаем список всех школ
import helpers
schools = helpers.jsonLoad('data/moskovskij.json')  
ids = [school['School'] for school in schools]

uni_names = []
for idn in ids:
    data = helpers.jsonLoad('data/uni_school_' + str(idn) + '.json')
    for student in data:
        uni_names.append(list(student.values())[0])
#%%
print('Всего вузов', len(uni_names))
uni_names = list(set(uni_names))
print('Уникальных вузов', len(uni_names))
print('\n'.join(uni_names))
