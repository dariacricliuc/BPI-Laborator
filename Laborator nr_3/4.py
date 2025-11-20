# Задача 4. Время года
luna=int(input("Введите номер месяца: "))
match luna:
    case 12|1|2:
        print("Зима")
    case 3|4|5:
        print("Весна")
    case 6|7|8:
        print("Лето")
    case 9|10|11:
        print("Осень")
    case _:
        print("Неизвестный месяц")