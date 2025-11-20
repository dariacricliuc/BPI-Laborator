# Задача 2. Количество делителей
n=int(input("Сколько чисел вводите?: "))
k=int(input("Сколько делителей?: "))
i=1
result=""
while i<=n:
    x=int(input("Введите число: "))
    divisors=0
    j=1
    while j<=x:
        if x%j==0:
            divisors=divisors+1
        j=j+1

    if divisors==k:
        if result=="":
            result=str(x)
        else:
            result=result+" "+str(x)
    i=i+1
print(result)