# def great_name(name):
#     if name[0].isupper():
#         return("Hello, "+ name)
#     else:
#         raise ValueError(name + " is  inappropriate name")
#
# print(great_name('andr'))
# print(great_name('Andr'))

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self,x):
        if x>0:
            super(PositiveList,self).append(x)
        else:
            raise NonPositiveError

b=PositiveList()
# b.append(-1)
b.append(5)
print(b)
