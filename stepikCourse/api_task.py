import requests
import os
#

with open('data/dataset_24476_3.txt','r') as f:
    data = f.read()

data = data.split()
print(data)
api_url = 'http://numbersapi.com/{}/math?json=true'

if os.path.exists('data/api_task.txt'):
    with open('data/api_task.txt','w') as report_file:
        report_file.write('')

with open('data/api_task.txt','a') as report_file:
    for number in data:
        params_url = api_url.format(number)
        resp = requests.get(params_url).json()
        if resp['found']:
            report_file.write('Interesting\n')
        else:
            report_file.write('Boring\n')

