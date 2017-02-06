#%%
'''
Необходимо установить модуль vk (https://pypi.python.org/pypi/vk)
Он может быть установлен через pip или скачен и установлен вручную
'''
import vk

#%%
'''
Для того чтобы выполнять запросы нужно авторизоваться, процедура авторизации
частично делается в ручную :(
Для начала нужно создать приложение на ВКонтакте (https://vk.com/editapp?act=create)
Платформа Веб-сайта
Адреса сайта http://ibsmirnov.com
Базовый домен ibsmirnov.com
В принципе, можно использовать и любой другой сайт, к которому есть доступ

После создания приложения нужно из настроек получить две переменных
ID приложения, которое будет обозначать APP_ID
и
Защищенный ключ, который будет обозначаться SECRET_KEY
'''
#%%
'''
Для того, чтобы провести авторизацию нужно выполнить следующие действия,
вначале вбить в строке браузера, подставив в строке браузера необходимый APP_ID

https://oauth.vk.com/authorize?client_id=APP_ID&redirect_uri=http://ibsmirnov.com&display=page&response_type=code

В принципе переход по ссылке можно автоматизировать в питоне через модуль webbrowser
import webbrowser
webbrowser.open_new_tab(url)
'''
#%%
'''
По ссылке произойдет переадресация на http://ibsmirnov.com/?code=CODE
нужно скопировать то, что будет на месте CODE и перейти по ссылке,
подставив значения переменных APP_ID, SECRET_KEY и CODE

https://oauth.vk.com/access_token?client_id=APP_ID&client_secret=SECRET_KEY&redirect_uri=http://ibsmirnov.com&response_type=code&code=CODE
'''
#%%
'''
Теперь осталось скопировать значение access_token в переменную token
и произвести авторизацию
'''
token = #INSERT VALUE HERE
session = vk.Session(access_token = token)
api = vk.API(session, v = '5.45')

#%%
'''
Теперь можно использовать методы API ВКонтакте (https://vk.com/dev/methods)
'''
# Загружаем пользователей из школы №366 (id на ВКонтакте 29) до 18 лет
vk_data = api.users.search(school = 29, age_to = 18)
users = vk_data['items']
# Выводим их имена
for user in users:
    print(user['first_name'], user['last_name'])

# Берем первого пользователя и получаем его посты
user_id = users[0]['id']
vk_data = api.wall.get(owner_id = user_id, offset = 0, count = 100, filter = 'owner')
posts = vk_data['items']
# Выводим содержимое постов
for post in posts:
    print(post['text'])

