# Задача 6. Значения функции на интервале
def f(x):
    return 3*x*x+x+2

x=-2

while x<=5:
    y=f(x)
    print("f(", x,")=", y)
    x=x+1