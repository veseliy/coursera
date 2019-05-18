# # TASK 1
# import sys
# import re

# for line in sys.stdin:
#     line = line.rstrip()
#     # process line
#     pattern = 'cat'
#     if len(re.findall(pattern, line)) >= 2:
#         print(line)
#


# # TASK 2
# import sys
# import re
#
# input = [
#     'cat',
#     'catapult and cat',
#     'catcat',
#     'concat',
#     'Cat',
#     '\"cat\"',
#     '!cat?'
#          ]
#
# # for line in sys.stdin:
# for line in input:
#     # line = line.rstrip()
#     # process line
#     pattern = r'\bcat\b'
#     search = re.search(pattern, line)
#     if search is not None:
#         print(line)

# # TASK 3
# import re
# import sys
#
# input_raw = [
#     'zabcz',
#     'zzz',
#     'zzxzz',
#     'zz',
#     'zxz',
#     'zzxzxxz',
#
# ]
#
# for line in sys.stdin:
#     line = line.rstrip()
#
# # for line in input_raw:
#     pattern = r'z.{3}z'
#     if re.search(pattern, line):
#         print(line)

# # TASK 4
# import re
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\\',line):
#         print(line)


# # TASK 5
# import re
# import sys
#
# input_raw = [
#     'blabla is a tandem repetition',
#     '123123 is good too',
#     'go go',
#     'aaa',
#     'aaaa',
#     'aaaaaaaa',
#     'test-test',
#     'ab.ab',
#     'ab-ab',
#     'a-a',
#     '123123',
#     'yy'
# ]
# # for line in sys.stdin:
# #     line = line.rstrip()
# for line in input_raw:
#     # all_incl = re.search(r'((\w+-?\B)\2\b)|((\w*)-\4\b)', line)
#     all_incl = re.search(r'\b(\w+)-?\1\b', line)
#     if all_incl is not None:
#         # print('lene = {}\nanswer = {}'.format(line,all_incl.groups()))
#         # print(all_incl)
#         print(re.findall(r'(\w+)-?\1\b', line))
#     # if re.search(r'(\w{2,}\B)\1\b', line):
#     #     print(line)

# # TASK 6
# import re
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'human','computer',line))

# # TASK 7
# import re
# import sys
#
# # for line in sys.stdin:
# #     line = line.rstrip()
#
# line = 'There’ll be no more "Aaaaaaaaaaaaaaa"'
# print(line)
# repl = re.sub(r'\b[Aa]+\b','argh',line,count=1)
# print(repl)
#
# line = 'AaAaAaA AaAaAaA'
# print(line)
# repl = re.sub(r'[Aa]+','argh',line,count=1)
# print(repl)

##TASK 9
# import re
# import sys
#
# line = 'this is a text'
# line2 = '"this\' !is. ?n1ce,'
#
# pattern = r'(\w)(\w)(\w+)?\b'
#
# print(re.sub(pattern,r'\2\1\3',line))
# print(re.sub(pattern,r'\2\1\3',line2))

## task 10
# import re
# import sys
#
# line = 'attraction'
# line2 = 'buzzzz'
#
# pattern = r'(\w)\1+'
#
# print(re.sub(pattern,r'\1',line))
# print(re.sub(pattern,r'\1',line2))

## task 11
import re
import sys

pattern = r'(0+101+)(010+1?)?|0+110+1?|(0+101+)(001+)+(010+1?)?'

pattern2 = r'(101+)(010+1)?|110+1|(101+)(001+010+1)?'

pattern_reverse = r'(10+10)?(1+01)|10+11|(10+101+00)?(1+01)'


pattern_reverse2 = r'(10+10)?(1+010+)|10+110+|(10+10)?(1+00)+(1+010+)'

pattern_version3 = r'(0*)|(0*(11)*0*)|(0*(1(01*0)*1)*0*)'
pattern_version5 = r'(0*(1(01*0)*1)*0*)*'

#'0*((1(01*0)*1)*)|((11)*)0*'



line = '1000'
line = '1'
line3 = '00101'
answ = '(1(01*0)*1|0)*'
line_tet = '101010000000'
pattern_version4 = r'0*((1(01*0)*1)*)|((11)*)0*'


line_rev = line[::-1]
print(line_rev)

line2 = '11000000000001011111111111101'

print(re.search(pattern_version5,line).group())
print(re.search(pattern_version5,line2).group())
# print(re.search(pattern_version5,line3))
# print(re.match(answ,line))
print(re.match(answ,line2))
# print(re.match(answ,line3))
# print(re.match(answ,line_tet).groups())
for g in re.search(answ,line2).groups():
    print(g == line2)