import re


# pattern = r'(<a.+href\s?=\s?\s?)(["\']?)(?!\.\.|\.)((\w+:)?\/{2})?((www\.)?[^: >]+(\2))'

# pattern2 = r'(<a.+href\s?=\s?\s?)(["\'])?([^>\'"]+)(\2)'


url = '<a href="test.com\'>'
url2 = '<a href="test#test"'


print(re.search(pattern2,url2).groups())
print(re.search(pattern,url2).groups())
print(re.search(pattern2,url).groups())