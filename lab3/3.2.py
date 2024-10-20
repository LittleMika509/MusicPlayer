years = int(input("Скільки тобі років: "))

if years < 6:
    print("Ще не школяр")
elif years >= 6 and years <= 9:
    print("Початкова школа")
elif years >= 10 and years <= 15:
    print("Середня школа")
elif years >= 16 and years <= 17:
    print("Старша школа")
else:
    print("Вже не школяр") 