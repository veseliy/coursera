# x = "hello\"world"
# print(x)
#
# x = r"hellow\nworld" #raw
#
#
# print(x)

import re

# print(re.match())
# print(re.search())
# print()

# pattern = r'a[abc]c'
# string = 'babc'
#
# # mathc_object = re.match(pattern, string)
# mathc_object = re.search(pattern, string)
# print(mathc_object)
#
# string = 'abc, acc, aac'
# all_inclusions = re.findall(pattern,string)
# print(all_inclusions)
#
#
# fixed_typos = re.sub(pattern, 'abc', string)
# print(fixed_typos)

# patter = r" english\?"
# string = "Do you speak english?"
# match = re.search(patter,string)
# print(match)

# [a-c]
# [^a-c]
# pattern = r'a[\w.]c'
# pattern = r'a.c'
# pattern = r'ab*a'
# pattern = r'ab+a'
# pattern = r'ab?a'
# pattern = r'ab{2,4}a'
# string = 'aa abc aba abba abbbba'
# pattern = r'a[ab]+a'
# pattern = r'a[ab]+?a'
# string = 'abaaba'
# # all_inclusive = re.findall(pattern, string)
# match = re.match(pattern, string)
# all_inclusive = re.findall(pattern, string)
# # print(all_inclusive)
# print(match)
# print(all_inclusive)

# pattern = r'((abc)|(test|text)*)'
# string = 'testtexttest'
# pattern = r'Hello (abc|test)'
# string = 'Hello abc'

# # pattern = r'(\w+)-\1'
# pattern = r'((\w+)-\2)'
# string = 'test-test chow-chow'
# # match =re.match(pattern, string)
# # duplicates = re.sub(pattern,r"\1", string)
# duplicates = re.findall(pattern, string)
# print(duplicates)

# print(match)
# print(match.groups())
# print(match.group(0))
# print(match.group(1))
# print(match.group())


# try:
#     print(mathc_object.span())
# except AttributeError as e:
#     print(e)
# raise AttributeError

import re

x = re.match(r'(te)*xt', 'TEXT', re.IGNORECASE | re.DEBUG)
print(x)
