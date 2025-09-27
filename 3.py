a=float(input("кількість хвилин:"))
if a<=50:
    print("100 грн")
elif a>50 and a<=100:
    print("150 грн")
elif a>100:
    k = 150 + (a - 100) * 2
    print(k, "грн")
else:
    print("Кількість хвилин була введена не правильно")