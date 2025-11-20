# Задача 7. Позитивные/негативные числа
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
    print("Негативных чисел нет")