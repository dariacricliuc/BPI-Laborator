'''# Задача 1. Сумма
n=int(input("Введите число n: "))
suma=0
i=2
while i<=n:
    suma=suma+i
    i=i+2

print("Сумма:", suma)'''



'''# Задача 2. Количество делителей
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
print(result)'''



'''# Задача 3. Чётные/нечётные числа
n=int(input("Сколько чисел вводите?: "))
count=1
suma_impare=0
suma_pare=0

while count<=n:
    numar=float(input("Введите число: "))
    
    if numar%2==1:
        suma_impare=suma_impare+numar
    else:
        suma_pare=suma_pare+numar
    count=count+1

if suma_pare!=0:
    raport=suma_impare/suma_pare
    print("Отношение:", raport)
else:
    print("Отношение не вычислимо")'''



'''# Задача 4. Кратность последней цифры
x=10 
while (x<=99):
    c=x%10
    if (c%3==0):
        print("Последняя цифра данного числа кратна трём")
    else:
        print("Последняя цифра данного числа не кратна трём")
    x=x+1'''



'''# Задача 5. Минимальное и максимальное значение среди чисел из строки
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
print("Максимальное значение:", maxim)'''



'''# Задача 6. Сумма всех цифр трёхзначного числа, кратная пяти
x=100
while (x<=999):
    a=x//100          
    b=(x//10)%10   
    c=x%10
    s=a+b+c
    if (s%5==0):
        print("Сумма цифр числа кратна пяти")
    else:
        print("Сумма цифр числа не кратна пяти")
    x=x+1'''



'''# Задача 7. Позитивные/негативные числа
count_poz=0
suma_poz=0
suma_neg=0
count_neg=0
i=1
while i<=10:
    numar=int(input("Введите число: "))
    if numar>0:
        count_poz+=1
        suma_poz+=numar
    elif numar<0:
        count_neg+=1
        suma_neg+=numar
    i=i+1

print("Позитивные числа:", count_poz)
print("Сумма позитивных чисел:", suma_poz)

if count_neg>0:
    media_neg=suma_neg/count_neg
    print("Среднее значение негативных чисел:", media_neg)
else:
    print("Негативных чисел нет")'''



'''# Задача 8. Сумма
n=int(input("Введите n: "))
suma=0
produs=1
i=1
while i<=n:
    produs=produs*i
    suma=suma+produs
    i=i+1

print("Сумма:", suma)'''



'''# Задача 9. Сумма
n=int(input("Введите n: "))
suma=0
i=1
while i<=n:
    if i%2==1:
        suma=suma+i
    else:
        suma=suma-i
    i=i+1

print("Сумма:", suma)'''



'''# Задача 10.
n=int(input("Введите число: "))
suma_divizori=0
i=1
while i<n:
    if n%i==0:
        suma_divizori=suma_divizori+i
    i=i+1

if suma_divizori==n:
    print(n, "- идеальное число")
else:
    print(n, "- не идеальное число")'''



'''# Задача 11. Разница цифр в квадрате
numar = 100
while numar<=999:
    primele_doua=numar//10
    ultima=numar%10  
    diferenta=primele_doua*primele_doua-ultima*ultima
    
    if diferenta==numar:
        print(primele_doua, "*", primele_doua, "-", ultima, "*", ultima, "=", numar)
    numar=numar+1'''



'''# Задача 12. Сумма цифр двухзначных чисел
n=int(input("Введите сумму цифр: "))
numar=10
while numar<=99:
    cifra1=numar//10     
    cifra2=numar%10     
    suma_cifre=cifra1+cifra2  
    
    if suma_cifre==n:       
        print(numar)   
    numar=numar+1'''



'''# Задача 13. Четырёхзначное число
numar=1000
while numar<=9999:
    mii=numar//1000
    sute=(numar//100)%10
    zeci=(numar//10)%10
    unitati=numar%10  
    
    if (mii==3) and (zeci==2) and (numar%9==0):
        print(numar)
    else:
        print("Число не соответсвует установленным правилам")
    numar=numar+1'''



'''# Задача 14. Поиск значения
n=int(input("Сколько чисел вводите?: "))
a=int(input("Какое значение ищете?: "))
count=0
i=1
while i<=n:
    x=int(input("Введите число: "))
    if x==a:
        count=count+1
    i=i+1

print("Значение", a, "появляется", count, "раз")'''



'''# Задача 15. Сумма двух последовательных цифр
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
    print("Невозможно")'''



'''# Задача 16. "Счастливый" билет
numar=100000
while numar<=999999:
    cifra1=numar//100000
    cifra2=(numar//10000)%10
    cifra3=(numar//1000)%10
    cifra4=(numar//100)%10
    cifra5=(numar//10)%10
    cifra6=numar%10
    suma_primele=cifra1+cifra2+cifra3
    suma_ultimele=cifra4+cifra5+cifra6
    
    if suma_primele==suma_ultimele:
        print(numar)
    numar=numar+1'''



'''# Задача 17. Сумма на счету
suma=1000
luna=1
while luna<=6:
    suma=suma+suma*0.02
    luna=luna+1

print("Сумма после шести месяцев:", suma)'''