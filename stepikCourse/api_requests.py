import requests
import json

api_url = 'http://api.openweathermap.org/data/2.5/weather'
city = input('City? ')

resp = requests.get(api_url,
                    params={
                        'q': city,
                        'appid': 'fbe56e091ab56b78d6a310dafe2dea0d',
                        'units': 'metric'
                    }
                    )
# print(resp.status_code, resp.text)
# print(resp.headers['Content-Type'])

data = resp.json()
template = 'Current temperature in {} is {}'
print(template.format(city,data['main']['temp']))
