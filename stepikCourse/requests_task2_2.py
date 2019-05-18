# put your python code here

import requests
import re
# a = 'http://pastebin.com/raw/7543p0ns'
with open('text.html','r',encoding='utf8') as f:
    a=f.read()

# html_text = requests.get(a).text
html_text = a
# html_text = requests.get(a).text


pattern = r'<a.+href=["\'](?!\.\./)([^" \'>]+)'


raw_urls = re.findall(pattern,html_text)
def url_clean(url):
    return re.sub(r'(\w+://)([^ /:\'"]+)([ /:\'"]?.+)?', r'\2', url)

cleaned_urls = [url_clean(url) for url in raw_urls]
cleaned_urls = list(set(cleaned_urls))
cleaned_urls.sort()
for u in cleaned_urls:
    print(u)



