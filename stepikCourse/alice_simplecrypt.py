import simplecrypt


with open("data/encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("data/passwords.txt", "r") as pas:
    paswords = pas.read()

paswords=paswords.split()
print(paswords)
# print(paswords)
for p in paswords:
    print(p)
    try:
        print(simplecrypt.decrypt(p,encrypted))
    except Exception as e:
        print(e)

