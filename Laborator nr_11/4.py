# Задача 4. Минимум в линии и максимум в колонне
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
    j+=1