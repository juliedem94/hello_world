#%%
import helpers
schools = helpers.loadXLSX('data/school', 'Лист1')
helpers.jsonSave('data/moskovskij.json', schools)