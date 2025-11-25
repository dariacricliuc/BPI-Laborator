# Задача 5. Количество цифр в числе
x=int(input("Введите число: "))
count=0
if (x==0):
    count=1
else:
    while (x>0):
        x=x//10
        count=count+1

print("Количество цифр:", count)