import random

list = []
for x in range(25):
    list.append(random.randint(-50, 50))
print(list)
a1 = [ ]
a2 = [ ]
for i in list:
    if i > 0:
        a1.append(i)
    else:
        a2.append(i)
print(a1)
print(a2)
