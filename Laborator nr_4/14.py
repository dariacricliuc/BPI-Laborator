# Задача 14. Поиск значения
n=int(input("Сколько чисел вводите?: "))
a=int(input("Какое значение ищете?: "))
count=0
i=1
while i<=n:
    x=int(input("Введите число: "))
    if x==a:
        count=count+1
    i=i+1

print("Значение", a, "появляется", count, "раз")