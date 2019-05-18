import requests
import json

client_app_name = 'andrapp'
client_id = 'c35bbd8126be435540e7'
client_secret = '5ca10084cae38f47b3fafe936399b810'


# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
with open('data/artists.txt','r') as artists_file:
    artists_list = artists_file.read()

artists_list = artists_list.split()

# artist = '4d8b92b34eb68a1b2c0003f4'
request_url = 'https://api.artsy.net/api/artists/{}'
result_list = []
for artist in artists_list:
    r = requests.get(request_url.format(artist), headers=headers)
    j = json.loads(r.text)
    result_list.append((j['birthday'],j['sortable_name']))

result_list.sort()
print(result_list)
# print(j['sortable_name'],j['birthday'])
with open('data/artists_result.txt','w',encoding='utf8') as artists_result:
    for a,d in result_list:
        artists_result.write(d+'\n')
