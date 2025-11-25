# Задача 6. Сортировка по убыванию и возрастанию
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

print("Vectorul obținut:", A)