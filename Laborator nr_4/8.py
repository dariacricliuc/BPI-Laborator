# Задача 8. Сумма
n=int(input("Введите n: "))
suma=0
produs=1
i=1
while i<=n:
    produs=produs*i
    suma=suma+produs
    i=i+1

print("Сумма:", suma)