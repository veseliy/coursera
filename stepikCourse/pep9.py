a = [1,2,3,345,345,24356,2456,246]
lower = 2
offset = 1
upper = 3
step = 1

a1 = a[lower + offset: upper + offset]
a2 = a[lower:: upper]
a3 = a[lower + offset: upper + offset]
a4 = a[lower + offset:upper + offset]
a5 = a[lower:upper], a[lower:upper:], a[lower::step]