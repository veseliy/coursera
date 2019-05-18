# winter
# is
# coming
# OMG: winter is coming


# tree={'BaseException': [''], 'Exception': ['BaseException'], 'LookupError': ['Exception'], 'KeyError': ['LookupError']}
tree={'winter': [], 'is': [], 'coming': [], 'OMG': ['winter','is','coming']}

tree={'winter': [], 'is': [], 'coming': [], 'OMG': ['winter', 'is', 'coming']}
a=0
def find_way(start,stop,tree):
    global a
    if start == "":
        a=False
    for node in tree.get(start):
        # print(node)
        # print(node==stop)
        if node == stop:
            a=True
        else:
            find_way(node,stop,tree)

# find_way('KeyError','BaseException',tree)
# print(tree.get('winter'))
# for i in tree.get('winter'):
#     print(i)
find_way('OMG','is',tree)
print(a)