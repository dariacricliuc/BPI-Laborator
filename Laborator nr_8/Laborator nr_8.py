'''# Задача 4. Соседние элементы с противоположными знаками
n=int(input("Câte numere?: "))
A=[0]*n
i=0

while i<n:
    A[i]=int(input("Introduceți numărul: "))
    i=i+1

count=0
i=1
while i<n:
    if (A[i-1]>0 and A[i]<0) or (A[i-1]<0 and A[i]>0):
        count=count+1
    i=i+1

print("Numărul de elemente vecine cu semn opus:", count)'''



'''# Задача 5. Произведение нечётных чисел на чётных позициях
n=int(input("Câte numere?: "))
A=[0]*n
i=0

while i<n:
    A[i]=int(input("Introduceți numărul: "))
    i=i+1

produs=1
i=0
while i<n:
    if i%2==0 and A[i]%2==1:
        produs=produs*A[i]
    i=i+1

print("Produsul valorilor impare de pe poziții pare:", produs)'''



'''# Задача 6. Сортировка по убыванию и возрастанию
n=int(input("Câte numere?: "))
k=int(input("Introduceți poziția k: "))
A=[0]*n
i=0

while i<n:
    A[i]=int(input("Introduceți numărul: "))
    i=i+1

i=0
while i<k:
    j=i+1
    while j<k:
        if A[i]<A[j]:
            A[i],A[j]=A[j],A[i]
        j=j+1
    i=i+1

i=k
while i<n:
    j=i+1
    while j<n:
        if A[i]>A[j]:
            A[i],A[j]=A[j],A[i]
        j=j+1
    i=i+1

print("Vectorul obținut:", A)'''