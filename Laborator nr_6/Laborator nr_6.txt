'''# Задача 4. Площадь и периметр окружности
def dreptunghi(p, q):
    aria=p*q
    perimetru=2*(p+q)
    print("Aria dreptunghiului:", aria)
    print("Perimetrul dreptunghiului:", perimetru)

p=float(input("Introduceți latura p: "))
q=float(input("Introduceți latura q: "))

dreptunghi(p, q)'''



'''# Задача 5. Площадь и периметр окружности
def cerc(r):
    aria=3.14*r*r
    perimetru=2*3.14*r
    print("Aria cercului:", aria)
    print("Perimetrul cercului:", perimetru)

r=float(input("Introduceți raza r: "))

cerc(r)'''



'''# Задача 6. Обратное число
def invers(x):
    inversat=0
    while x>0:
        c=x%10
        inversat=inversat*10+c
        x=x//10
    print("Numărul inversat este:", inversat)

x=int(input("Introduceți un număr natural: "))

invers(x)'''