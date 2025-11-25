# Задача 6. Замена первой строки строкой с элементом ноль
n=int(input("n linii: "))
m=int(input("m coloane: "))

A=[[0]*m for _ in range(n)]
i=0
while i<n:
    j=0
    while j<m:
        A[i][j]=int(input("Element: "))
        j+=1
    i+=1

rand_zero=-1
i=0
while i<n:
    j=0
    while j<m:
        if A[i][j]==0:
            rand_zero=i
            break
        j+= 1
    if rand_zero!=-1:
        break
    i+=1

if rand_zero!=-1 and rand_zero!=0:
    j=0
    while j<m:
        temp=A[0][j]
        A[0][j]=A[rand_zero][j]
        A[rand_zero][j]=temp
        j+=1

i=0
while i<n:
    j=0
    while j<m:
        print(A[i][j], end="")
        j+=1
    print()
    i += 1