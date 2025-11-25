# Задача 4. Принадлежность элементов интервалу [1; m]
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
    print("NU toate numerele sunt în intervalul [1;", m,"]")