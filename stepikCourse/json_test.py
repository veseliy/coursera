import json

# json.dumps()
# json.loads()

# json.load()

# input_data = [
#     {"name": "A", "parents": []},
#     {"name": "B", "parents": ["A", "C"]},
#     {"name": "C", "parents": ["A"]}
#               ]

input_data = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]

# input_data = json.loads(input_data)

def find_way(cl,tree):
    global path
    for node in tree:
        if cl in node['parents']:
            path.append(node['name'])
            find_way(node['name'],tree)
        else:
            pass
    return path

class_ways = {}
for w in input_data:
    path = []
    class_ways[w['name']] = find_way(w['name'],input_data)

class_ways = dict(sorted(class_ways.items()))
for i in class_ways.keys():
    print('{} : {}'.format(i,len(set(class_ways.get(i))) + 1))
