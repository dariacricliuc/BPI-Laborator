# Задача 15. Сумма двух последовательных цифр
n=int(input("Введите число n: "))
gasit=False
i=1
while i<n:
    if i+(i+1)==n:
        print(n, "=", i, "+", i+1)
        gasit=True
        break
    i=i+1

if not gasit:
    print("Невозможно")