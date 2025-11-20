# Задача 5. Минимальное и максимальное значение среди чисел из строки
n=int(input("Введите количество чисел: "))
x=float(input("Введите первое число: "))
minim=x
maxim=x
i=1
while (i<n):
    x=float(input("Введите следующие числа: "))
    if x<minim:
        minim=x
    if x>maxim:
        maxim=x
    i=i+1

print("Минимальное значение:", minim)
print("Максимальное значение:", maxim)