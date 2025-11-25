# Задача 5. Произведение нечётных чисел на чётных позициях
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

print("Produsul valorilor impare de pe poziții pare:", produs)