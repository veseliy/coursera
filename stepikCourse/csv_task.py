import csv
import re
from collections import Counter

with open('./data/Crimes.csv','r') as f:
    df = csv.reader(f)
    lines = [x for x in df]

print(lines[0])
cnt=0
crimes = []
for line in lines[1:]:
    if line[2][6:10]=='2015':
        crimes.append(line[5])


print(Counter(crimes).most_common(1))



