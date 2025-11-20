# Задача 2. Соответствие дня десятилетию
zi=int(input("Введите день: "))
match zi:
    case 1|2|3|4|5|6|7|8|9|10:
        print("Decada I")
    case 11|12|13|14|15|16|17|18|19|20:
        print("Decada II")
    case 21|22|23|24|25|26|27|28|29|30:
        print("Decada III")
    case 31:
        print("Decada IV")
    case _:
        print("Неизвестный день")