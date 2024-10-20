ls = list(range(0, 56, 2))
print (ls)
ls2 = [ ]
for x in ls:
    ls2.append(x*2)
print (ls2)
a1 = sum(ls2)
a2 = min(ls2)
a3 = max(ls2)
result = {"sum": a1, "min": a2, "max": a3}
print(result)
ls3 = tuple(ls2)
ls4 = str(ls2)
print(type(ls2))
print(type(ls3))
print(type(ls4))