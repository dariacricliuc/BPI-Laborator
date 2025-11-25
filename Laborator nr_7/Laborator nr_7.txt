'''# Задача 4. Функция MAX
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
print("Rezultatul este:", rezultat)'''



'''# Задача 5. Палиндромы 
def PALINDROM(n):
    original=n
    invers=0
    while n>0:
        cifra=n%10
        invers=invers*10+cifra
        n=n//10
    return original==invers

numar=100

while numar<=300:
    if PALINDROM(numar):
        patrat=numar*numar
        if PALINDROM(patrat):
            print(numar)
    numar+=1'''



'''# Задача 6. Значения функции на интервале
def f(x):
    return 3*x*x+x+2

x=-2

while x<=5:
    y=f(x)
    print("f(", x,")=", y)
    x=x+1'''