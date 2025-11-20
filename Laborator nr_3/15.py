direction=input("Введите начальное направление (N, S, E, V): ")
instruction=int(input("Введите инструкцию (0 - продолжить, 1 - влево, 2 - вправо): "))

if direction not in ("N", "S", "E", "V") or instruction not in (0, 1, 2):
    print("Ошибка: перепроверьте введённые данные")
else:
    match instruction:
        case 0:
            rezultat=direction
            
        case 1:
            match direction:
                case "N":
                    rezultat="V"
                case "V":
                    rezultat="S"
                case "S":
                    rezultat="E"
                case "E":
                    rezultat="N"
                    
        case 2:
            match direction:
                case "N":
                    rezultat="E"
                case "E":
                    rezultat="S"
                case "S":
                    rezultat="V"
                case "V":
                    rezultat="N"

print("Робот теперь движется следующим образом:", rezultat)