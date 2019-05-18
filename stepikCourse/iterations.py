lst=[1,2,3,4,5,6]

book={
    'title':'The Langoliers',
    'author':'Stephen King',
    'yaer_published':1990
}

string='Hellos world'




# iterator=iter(book)
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


for i in lst:
    print(i)

it = iter(lst)

while True:
    try:
        i=next(it)
        print(i)
    except Exception as e:
        print(e)
        break


