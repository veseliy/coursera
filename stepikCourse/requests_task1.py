import requests
import re

a = input()
b = input()

# a = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# b = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

res = requests.get(a)
content = res.text
# print(content)
pattern = r'href=[\'"]?([^\'" >]+)'

urls_list = re.findall(pattern,content)
# print(urls_list)
all_urls_data = []
for url in urls_list:
    res = requests.get(url)
    all_urls_data.append(res.text)

all_urls_data2 = ' '.join(all_urls_data)
urls_list = re.findall(pattern, all_urls_data2)
if b in urls_list:
    print('Yes')
else:
    print('No')


# pattern = r'href=.+"'
#
# string = 'href="http://google.com">'
# print(re.findall(pattern,string))