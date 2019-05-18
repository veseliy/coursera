def get_parents(s):
    try:
        return(s.split(":")[1].split())
    except IndexError:
        return []

def find_way(start,stop,tree):
    global a
    if start == "":
        a=False
    for node in tree.get(start):
        if node == stop:
            a=True
        else:
            find_way(node,stop,tree)

n=int(input())

input_list=[]
class_tree={}
for i in range(n):
    s=input()
    class_tree[s.split(":")[0].replace(' ','')]=get_parents(s)


m=int(input())
bad_list=[]
input_list.append(input())

for i in range(m-1):
    s1=input()
    for j in input_list:
        a=0
        find_way(s1, j, class_tree)
        try:
            if a:
                bad_list.append(s1)
                break
        except:
            continue
    input_list.append(s1)

for i in bad_list:
    print(i)

