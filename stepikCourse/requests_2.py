import requests

# res = requests.get('http://docs.python.org/3.6/_static/py.png')
# print(res.status_code)
# print(res.headers['Content-Type'])
#
# print(res.content)
#
# with open('python.png','wb') as f:
#     f.write(res.content)

res = requests.get('http://yandex.ru/search/',
                   params={'text': 'stepic'})
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)
print(res.text)
print(res.url)

# with open('python.png','wb') as f:
#     f.write(res.content)