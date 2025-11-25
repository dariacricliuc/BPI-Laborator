# Задача 4. Соседние элементы с противоположными знаками
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

print("Numărul de elemente vecine cu semn opus:", count)