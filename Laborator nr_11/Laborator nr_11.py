'''# Задача 4. Минимум в линии и максимум в колонне
n=int(input())
m=int(input())

A=[[0]*m for _ in range(n)]
i=0
while i<n:
    j=0
    while j<m:
        A[i][j]=int(input())
        j+=1
    i+=1

i=0
while i<n:
    min_lin=A[i][0]
    j=1
    while j<m:
        if A[i][j]<min_lin:
            min_lin=A[i][j]
        j+=1
    print(min_lin)
    i+=1

j=0
while j<m:
    max_col=A[0][j]
    i=1
    while i<n:
        if A[i][j]>max_col:
            max_col=A[i][j]
        i+=1
    print(max_col)
    j+=1'''



'''# Задача 5. Создание матрицы, зная число n
n=int(input("Introduceți n: "))
matrice=[[0]*n for _ in range(n)]
i=0
while i<n:
    j=0
    while j<n:
        element=(i+j)%n+1
        matrice[i][j]=element
        j+=1
    i+=1

i=0
while i<n:
    j=0
    while j<n:
        print(matrice[i][j], end="")
        j+=1
    print()
    i+=1'''



'''# Задача 6. Замена первой строки строкой с элементом ноль
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
    i += 1'''