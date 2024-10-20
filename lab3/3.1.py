a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))

if a == b == c:
    print(3)
elif a == b or a == c or c == b:
    print(2)
else:
    print(0)