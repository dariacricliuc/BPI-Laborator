# Задача 4. Площадь и периметр прямоугольника
def dreptunghi(p, q):
    aria=p*q
    perimetru=2*(p+q)
    print("Aria dreptunghiului:", aria)
    print("Perimetrul dreptunghiului:", perimetru)

p=float(input("Introduceți latura p: "))
q=float(input("Introduceți latura q: "))

dreptunghi(p, q)