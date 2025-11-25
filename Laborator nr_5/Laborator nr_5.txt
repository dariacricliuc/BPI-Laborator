'''# Задача 4. Ввод чисел и подсчёт трёхзначных, пока не "0"
count=0

while True:
    x=int(input("Введите число: "))
    if x==0:
        break
    if 100<=x<=999:
        count=count+1

print("Количество трёхзначных чисел:", count)'''



'''# Задача 5. Количество цифр в числе
x=int(input("Введите число: "))
x=abs(x)
count=0
if (x==0):
    count=1
else:
    while (x>0):
        x=x//10
        count=count+1

print("Количество цифр:", count)'''



'''# Задача 6. Количество чётных и нечётных цифр в числе
x=int(input("Введите число: "))
x=abs(x)
p=0
n=0

if (x==0):
    p=1
else:
    while (x>0):
        c=x%10
        if (c%2==0):
            p=p+1
        else:
            n=n+1
        x=x//10

print("Чётных цифр:", p)
print("Нечётных цифр:", n)'''