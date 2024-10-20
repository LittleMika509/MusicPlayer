import math

t = 2.5
while t <= 9:
    y = (1.5 * t - math.log(2*t))/(3 * t + 1)
    print("t = ", t,", y = ", y)
    t += 0.8

t = 0.8
for _ in range(6):
    y = (1.5 * t - math.log(2 * t))/(3 * t + 1)
    print("t = ", t,", y = ", y)
    t += 1.2














