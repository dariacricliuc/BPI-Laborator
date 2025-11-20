# Задача 8. Меню
print("Меню:")
print("1. Сумма")
print("2. Произведение")
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
optiune=int(input("Выберите опцию (1 или 2): "))
match optiune:
    case 1:
        rezultat=a+b
        print("Результат:", rezultat)
    case 2:
        rezultat=a*b
        print("Результат:", rezultat)
    case _:
        print("Неизвестная опция")