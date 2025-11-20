'''# Задача 1. Определение символа 
ch=input("Введите один символ: ")
match ch:
    case 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'|'i'|'j'|'k'|'l'|'m'|'n'|'o'|'p'|'q'|'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y'|'z'|'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J'|'K'|'L'|'M'|'N'|'O'|'P'|'Q'|'R'|'S'|'T'|'U'|'V'|'W'|'X'|'Y'|'Z':
        print("Буква")
    case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
        print("Цифра")
    case '+'|'-'|'*'|'/':
        print("Оператор")
    case _:
        print("Неизвестный символ")'''



'''# Задача 2. Соответствие дня десятилетию
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
        print("Неизвестный день")'''



'''# Задача 3. Гласная/согласная буква
ch=input("Введите символ: ")
match ch:
    case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print("Гласная")
    case 'b'|'c'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'y'|'z'|'B'|'C'|'D'|'F'|'G'|'H'|'J'|'K'|'L'|'M'|'N'|'P'|'Q'|'R'|'S'|'T'|'V'|'W'|'X'|'Y'|'Z':
        print("Согласная")
    case _:
        print("Символ не является буквой")'''



'''# Задача 4. Время года
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
        print("Неизвестный месяц")'''



'''# Задача 5. Ввод цифры и вывод буквами
cifra=int(input("Введите цифру: "))
if (cifra>=0) and (cifra<=9):
    match cifra:
        case 0: 
            print ("Ноль")
        case 1:
            print("Один")
        case 2:
            print("Два")
        case 3:
            print("Три")
        case 4:
            print("Четыре")
        case 5:
            print("Пять")
        case 6:
            print("Шесть")
        case 7:
            print("Семь")
        case 8:
            print("Восемь")
        case 9:
            print("Девять")
else:
    print("Ошибка: перепроверьте введённую цифру")'''



'''# Задача 6. Длина в метрах
lungime=float(input("Введите длину: "))
unitate=int(input("Введите единицу измерения (1-дм, 2-км, 3-м, 4-мм, 5-см): "))
match unitate:
    case 1:
        metri=lungime/10
    case 2:
        metri=lungime*1000
    case 3:
        metri=lungime
    case 4:
        metri=lungime/1000
    case 5:
        metri=lungime/100
    case _:
        print("Неизвестная единица измерения")
        metri=None

if metri is not None:
    print("Длина в метрах: ", metri)'''



'''# Задача 7. Трёхзначное число буквами
num=int(input("Введите натуральное и трёхзначное число из интервала от 100 до 999: "))
if (num>=100) and (num<=999):
    c_1=num//100
    c_2=(num//10)%10
    c_3=num%10
    print("Полученный результат: ", end="") 
    
    match c_1:
        case 1: 
            print("Сто", end="")
        case 2:
            print("Двести", end="")
        case 3:
            print("Триста", end="")
        case 4:
            print("Четыреста", end="")
        case 5:
            print("Пятьсот", end="")
        case 6:
            print("Шестьсот", end="")
        case 7:
            print("Семьсот", end="")
        case 8:
            print("Восемьсот", end="")
        case 9:
            print("Девятьсот", end="")
            
    if c_2 == 1:
        match c_3:  
            case 0: 
                print(" десять", end="")
            case 1:
                print(" одинадцать", end="")
            case 2:
                print(" двенадцать", end="")
            case 3:
                print(" тринадцать", end="")
            case 4:
                print(" четырнадцать", end="")
            case 5:
                print(" пятнадцать", end="")
            case 6:
                print(" шестнадцать", end="")
            case 7:
                print(" семнадцать", end="")
            case 8:
                print(" восемнадцать", end="")
            case 9:
                print(" девятнадцать", end="")  
                
    else:
        match c_2:
            case 0:
                pass   
            case 2: 
                print(" двадцать", end="")
            case 3:
                print(" тридцать", end="")
            case 4:
                print(" сорок", end="")
            case 5:
                print(" пятьдесят", end="")
            case 6:
                print(" шестьдесят", end="")
            case 7:
                print(" семьдесят", end="")
            case 8:
                print(" восемьдесят", end="")
            case 9:
                print(" девяносто", end="")
                    
        match c_3:
            case 0:
                pass
            case 1:
                print(" один", end="")
            case 2:
                print(" два", end="")
            case 3:
                print(" три", end="")
            case 4:
                print(" четыре", end="")
            case 5:
                print(" пять", end="")
            case 6:
                print(" шесть", end="")
            case 7:
                print(" семь", end="")
            case 8:
                print(" восемь", end="")
            case 9:
                print(" девять", end="")
                    
else:
    print("Ошибка: перепроверьте введённое число")'''



'''# Задача 8. Меню
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
        print("Неизвестная опция")'''



'''# Задача 9. Величины окружности
valoare=float(input("Введите значение: "))
element=int(input("Введите элемент (1-радиус, 2-диаметр, 3-длина, 4-площадь): "))
П=3.14
match element:
    case 1:
        r=valoare
        d=2*r
        l=2*П*r
        a=П*r*r
    case 2:
        d=valoare
        r=d/2
        l=2*П*r
        a=П*r*r
    case 3:
        l=valoare
        r=l/(2*П)
        d=2*r
        a=П*r*r
    case 4:
        a=valoare
        r=(a/П)**0.5
        d=2*r
        l=2*П*r
    case _:
        print("Element invalid")
        r=d=l=a=None

if r is not None:
    print("Радиус:", r)
    print("Диаметр:", d)
    print("Длина:", l)
    print("Площадь:", a)'''



'''# Задача 10. Оценка
nota=int(input("Введите оценку (1-10): "))
match nota:
    case 1|2|3|4:
        print("Неудовлетворительно")
    case 5|6:
        print("Удовлетворительно")
    case 7|8:
        print("Хорошо")
    case 9|10:
        print("Очень хорошо")
    case _:
        print("Неизвестная оценка")'''



'''# Задача 11.
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
        print("Неизвестная опция")'''



'''# Задача 12. Вес
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
    print("Вес в килограммах:", kg)'''



'''# Задача 13. Вычисление даты следующего дня
d=int(input("Введите день: "))
m=int(input("Введите месяц: "))
g=int(input("Введите год: "))
match m:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        total=31
    case 4 | 6 | 9 | 11:
        total=30
    case 2:
        if g%4==0:
            total=29
        else:
            total=28
    case _:
        print("Неверно введённый месяц")
        exit()

d=d+1
if d>total:
    d=1
    m=m+1
    if m>12:
        m=1
        g=g+1

print("Дата следующего дня:", d, m, g)'''



'''# Задача 14. Ввод одной из четырёх характеристик треугольника
n=int(input("Введите одну из четырёх характеристик равнобедренного и прямоугольного треугольника: 1 - катет; 2 - гипотенуза; 3 - высота, опущенная на гипотенузу; 4 - площадь треугольника: "))
x=float(input("Введите значение характеристики: "))

if ((n<1) or (n>4)) or x<0:
    print("Ошибка: неверный номер характеристики или отрицательное значение характеристики")
else:
    match n:
        case 1:
            a=x
            c=((a**2)+(a**2))**0.5
            h=((a**2)-(c/2)**2)**0.5
            s=(a*a)/2

        case 2:
            c=x
            a=c/(2**0.5)
            h=((a**2)-(c/2)**2)**0.5
            s=(a*a)/2

        case 3:
            h=x
            a=h*(2**0.5)
            c=((a**2)+(a**2))**0.5
            s=(a*a)/2

        case 4:
            s=x
            a=(2*s)**0.5
            c=((a**2)+(a**2))**0.5
            h=((a**2)-(c/2)**2)**0.5

print("Катет a:", a)
print("Гипотенуза c:", c)
print("Высота h:", h)
print("Площадь s:", s)'''



'''# Задача 15. Движение робота по введённым значениям
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

print("Робот теперь движется следующим образом:", rezultat)'''