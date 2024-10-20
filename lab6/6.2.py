import math

t = -4
while t <= 0:
    u = 1.3 * t - math.sin(t)
    print("t = ",t, ", u(t) = ", u)
    t += 1

t = 0.5
while t <= 4:
    u = math.log10(t + math.sqrt(t))
    print("t = ",t, ", u(t) = ", u)
    t += 0.5