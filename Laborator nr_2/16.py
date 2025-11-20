# Задача 16. Принадлежность точки прямоугольнику
xs=float(input("Введите xs: "))
ys=float(input("Введите ys: "))
xd=float(input("Введите xd: "))
yd=float(input("Введите yd: "))

x=float(input("Введите координаты х: "))
y=float(input("Введите координаты у: "))

if (xs<=x<=xd) and (ys<=y<=yd):
    print("Точка находится внутри прямоугольника")
else:
    print("Точка не находится внутри прямоугольника")