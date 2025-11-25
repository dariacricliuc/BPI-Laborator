# Задача 6. Позиция последнего элемента, равная нулю
n=int(input("Câte numere?: "))
A=[0]*n
i=0

while i<n:
    A[i]=int(input("Introduceți numărul: "))
    i=i+1

gasit=False
i=n-1

while i>=0:
    if A[i]==0:
        print("Ultimul element egal cu 0 este pe poziția", i)
        gasit=True
        break
    i=i-1

if not gasit:
    print("Nu există elemente egale cu 0")