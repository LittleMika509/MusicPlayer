import math
pi = math.pi
sqrt = math.sqrt

x = float(input("Введіть х: "))

if pi <= x and x < 8.5:
    y = 2**(x-1) + 2.71
elif 8.5 < x and x < pi:
    y = sqrt(abs(pi - x))
elif 8.5 <= abs(x):
    y = 2.7
else:
    y = False
print(y)