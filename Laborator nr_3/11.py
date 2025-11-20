# Задача 11.
lungime=float(input("Введите длину: "))
latime = float(input("Введите ширину: "))
optiune = int(input("Выберите опцию (1-периметр, 2-площадь, 3-диагональ): "))
match optiune:
    case 1:
        perimetru=2*(lungime+latime)
        print("Perimetrul:", perimetru)
    case 2:
        arie=lungime*latime
        print("Aria:", arie)
    case 3:
        diagonala=(lungime**2+latime**2)**0.5
        print("Diagonala:", diagonala)
    case _:
        print("Неизвестная опция")