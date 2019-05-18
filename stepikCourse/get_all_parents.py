# class_tree={'BaseException': '', 'Exception': 'BaseException', 'LookupError': 'Exception', 'KeyError': 'LookupError'}
#
#
# print(class_tree.get('BaseException')=='')
#
# def get_parent(child,c):
#     global class_parents_list
#     if class_tree.get(child)=='':
#         pass
#         # print('final class tree', class_parents_list)
#         # return class_parents_list
#     else:
#         class_parents_list.append(class_tree.get(child))
#         # print('class tree',class_parents_list)
#         get_parent(class_tree.get(child), class_tree)
#
# all_parents_dict={}
# for k in class_tree.keys():
#     class_parents_list = []
#     get_parent(k,class_tree)
#     all_parents_dict[k]=class_parents_list
#
# print('final class tree final', all_parents_dict)


import datetime

x=input()
x=x.split()
dif=input()
first_date=datetime.date(int(x[0]),int(x[1]),int(x[2]))

last_date=first_date+datetime.timedelta(int(dif))
print(last_date.year,last_date.month,last_date.day)
