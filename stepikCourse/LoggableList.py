import os

folders = []
for i in os.walk('main'):
    if any(".py" in s for s in i[2]):
        folders.append(i[0])
# print(folders)
folders.sort()
# folders_sorted = folders.sort()
# print(folders)
with open('res.txt','w') as f:
    for i in folders:
        f.write(i + '\n')


