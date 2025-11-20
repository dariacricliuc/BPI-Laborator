# Задача 11. Рост детей
H1=int(input("Введите рост Ионела: "))
H2=int(input("Введите рост Гигела: "))
H3=int(input("Введите рост Дануца: "))
if H1<=H2 and H1<=H3:
    if H2<=H3:
        print("Ionel, Gigel, Danuț")
    else:
        print("Ionel, Danuț, Gigel")
elif H2<=H1 and H2<=H3:
    if H1<=H3:
        print("Gigel, Ionel, Danuț")
    else:
        print("Gigel, Danuț, Ionel")
else:
    if H1<=H2:
        print("Danuț, Ionel, Gigel")
    else:
        print("Danuț, Gigel, Ionel")