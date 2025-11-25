# Задача 4. Ввод чисел и подсчёт трёхзначных, пока не "0"
count=0

while True:
    x=int(input("Введите число: "))
    if x==0:
        break
    if 100<=x<=999:
        count=count+1

print("Количество трёхзначных чисел:", count)