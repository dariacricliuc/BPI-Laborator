# Задача 5. Площадь и периметр окружности
def cerc(r):
    aria=3.14*r*r
    perimetru=2*3.14*r
    print("Aria cercului:", aria)
    print("Perimetrul cercului:", perimetru)

r=float(input("Introduceți raza r: "))

cerc(r)