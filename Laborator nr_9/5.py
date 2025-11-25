# Задача 5. Сравнение позиции первого элемента с числом k
k=int(input("Introduceți k: "))
n=int(input("Câte numere?: "))
A=[0]*n
i=0

while i<n:
    A[i]=int(input("Introduceți numărul: "))
    i=i+1

gasit=False
i=0
while i<n:
    if A[i]>k:
        print("Primul element mai mare decât", k, "este pe poziția", i)
        gasit=True
        break
    i=i+1

if not gasit:
    print("Nu există elemente mai mari decât", k)