# s = input()
# a = input()
# b = input()
# i = 0
# while s.find(a) >= 0:
#     s = s.replace(a, b)
#     i += 1
#     if i == 1000:
#         i = 'Impossible'
#         break
# print(i)

s = input()
t = input()
i = 0
pos = 0
while s.find(t, pos) >= 0:
    pos = s.find(t, pos) + 1
    # s = s[s.find(t, i + len(t) - 1):]
    # print(s)
    i+=1



print(i)
