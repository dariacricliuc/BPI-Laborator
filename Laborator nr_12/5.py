# Задача 5. Результаты экзаменов
n = int(input("Câți elevi? "))
elevi = [()] * n

i = 0
while i < n:
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    elevi[i] = (nume, prenume, nota1, nota2, media)
    i += 1

n=int(input("Câți elevi? "))
elevi=[()]*n

i=0
while i<n:
    nume=input("Nume: ")
    prenume=input("Prenume: ")
    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    media=(nota1+nota2) / 2
    elevi[i]=(nume, prenume, nota1, nota2, media)
    i+=1

respinși=[()]*n
count_respinsi=0
i=0
while i<n:
    if elevi[i][4]<5.00:
        respinși[count_respinsi]=elevi[i]
        count_respinsi+=1
    i+=1

i=0
while i<count_respinsi-1:
    j=i+1
    while j<count_respinsi:
        if respinși[i][0]>respinși[j][0]:
            respinși[i], respinși[j]=respinși[j], respinși[i]
        j+=1
    i+=1

print("Elevi respinși:")
i=0
while i<count_respinsi:
    print(respinși[i][0], respinși[i][1], ":", respinși[i][4])
    i+=1