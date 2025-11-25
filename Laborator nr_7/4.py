# Задача 4. Функция MAX
def MAX(x, y, z):
    if x>=y and x>=z:
        return x
    elif y>=z:
        return y
    else:
        return z

a=float(input("Introduceți a: "))
b=float(input("Introduceți b: "))
c=float(input("Introduceți c: "))

rezultat=MAX(a-b, a, a+b)+MAX(a, b+c, a-c)
print("Rezultatul este:", rezultat)