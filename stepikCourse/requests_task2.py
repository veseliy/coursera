import re
import requests

# a = input()
a = 'http://pastebin.com/raw/hfMThaGb'

# pattern = r'(<a.+href=)(["\']?)(?!\.\.|\.)((\w+:)?\/{2})?((www\.)?[A-Za-z\.-]+)([/:>?\'"])'
url_pattern = r'(<a.+href=(["\'])?(\w+:\/{2})?([^:\'">]+))'
domen_pattern = r'[^:/]+'

html_text = requests.get(a).text
url_list = re.findall(url_pattern,html_text)
url_list = [re.search(domen_pattern,x[3]).group() for x in url_list]
url_list = [x for x in url_list if x not in ('',' ','.','..')]
url_list = list(set(url_list))
url_list.sort()
for u in url_list:
    print(u)

