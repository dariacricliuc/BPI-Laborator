# Задача 6. Обратное число
def invers(x):
    inversat=0
    while x>0:
        c=x%10
        inversat=inversat*10+c
        x=x//10
    print("Numărul inversat este:", inversat)

x=int(input("Introduceți un număr natural: "))

invers(x)