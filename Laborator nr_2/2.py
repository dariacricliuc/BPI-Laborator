# Задача 2. Тип треугольника
a=float(input("Введите a: "))
b=float(input("Введите b: "))
c=float(input("Введите c: "))
if not(a+b>c and a+c>b and b+c>a) and not(a>0 and b>0 and c>0):
    print("Треугольник не существует")
    
else:
    if (a==b==c):
        print("Треугольник равносторонний")
    else:
        if a==b or b==c or a==c:
            print("Треугольник равнобедренный")
        else:
            if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (b**2)+(c**2)==(a**2):
                print("Треугольник прямоугольный")
            else:
                print("Треугольник произвольный")