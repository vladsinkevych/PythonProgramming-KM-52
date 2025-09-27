items = input("Введіть предмети через пробіл: ").split()
if len(items) == 0:
    print("Список порожній")
elif len(items) == 1:
    print(items[0])
elif len(items) == 2:
    print(items[0], "and", items[1])
else:
    print(", ".join(items[:-1]), "and", items[-1])