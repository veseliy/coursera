_Greating='Fuck'
class BadName(Exception):
    pass

def greatname(name):
    if name[0].isupper():
        return Greating+name
    else:
        raise BadName(name+" is inappropriate name")

# if __name__=='__main__':
#     print(greatname('Andr'))


# print(__name__)
# __all__=['BadName','greatname']