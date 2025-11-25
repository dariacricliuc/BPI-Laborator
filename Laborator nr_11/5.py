# Задача 5. Создание матрицы, зная число n
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
    i+=1