s = float(input("Введите стоимость подписки на онлайн-кинотеатр: "))
p = float(input("Введите стоимость пиццы: "))
m = float(input("Введите зарплату: "))

if s + p <= m:
    print("Да")
else:
    print("Нет")