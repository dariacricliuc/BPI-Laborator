# Задача 9. Сумма
n=int(input("Введите n: "))
suma=0
i=1
while i<=n:
    if i%2==1:
        suma=suma+i
    else:
        suma=suma-i
    i=i+1

print("Сумма:", suma)