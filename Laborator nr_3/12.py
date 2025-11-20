# Задача 12. Вес
greutate=float(input("Введите вес: "))
unitate=int(input("Введите единицу измерения (1-кг, 2-мг, 3-г, 4-т): "))
match unitate:
    case 1:
        kg=greutate
    case 2:
        kg=greutate/1000000
    case 3:
        kg=greutate/1000
    case 4: 
        kg=greutate*1000
    case _:
        print("Неизвестная единица измерения")
        kg=None

if kg is not None:
    print("Вес в килограммах:", kg)