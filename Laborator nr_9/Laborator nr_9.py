'''# Задача 4. Принадлежность элементов интервалу [1; m]
n=int(input("Câte numere?: "))
m=int(input("Introduceți m: "))
A=[0]*n
i=0

while i<n:
    A[i]=int(input("Introduceți numărul: "))
    i=i+1

toate_in_interval=True
i=0
while i<n:
    if A[i]<1 or A[i]>m:
        toate_in_interval=False
    i=i+1

if toate_in_interval:
    print("Toate numerele sunt în intervalul [1;", m,"]")
else:
    print("NU toate numerele sunt în intervalul [1;", m,"]")'''



'''# Задача 5. Сравнение позиции первого элемента с числом k
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
    print("Nu există elemente mai mari decât", k)'''



'''# Задача 6. Позиция последнего элемента, равная нулю
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
    print("Nu există elemente egale cu 0")'''