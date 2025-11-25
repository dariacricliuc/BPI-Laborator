'''# Задача 4. Данные работников одной фирмы
n=int(input("Câți angajați? "))
angajati=[()]*n

i=0
while i<n:
    nume=input("Nume: ")
    prenume=input("Prenume: ")
    salariu=float(input("Salariu: "))
    avans=float(input("Avans: "))
    angajati[i]=(nume, prenume, salariu, avans)
    i+=1

print("Suma rămasă:")
i=0
while i<n:
    ramas=angajati[i][2]-angajati[i][3]
    print(angajati[i][0], angajati[i][1], ":", ramas)
    i+=1

i=0
while i<n-1:
    j=i+1
    while j<n:
        if angajati[i][2]>angajati[j][2]:
            angajati[i], angajati[j]=angajati[j], angajati[i]
        j+=1
    i+=1

print("Angajați ordonați:")
i=0
while i<n:
    print(angajati[i][0], angajati[i][1], ":", angajati[i][2])
    i+=1

total=0
i=0
while i<n:
    total+=angajati[i][2]
    i+=1

medie=total/n
print("Salariul mediu:", medie)'''



'''# Задача 5. Результаты экзаменов
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
    i+=1'''



'''# Задача 6. Данные о библиотеке
n=int(input("Câte cărți? "))
carti=[()]*n

i=0
while i<n:
    titlu=input("Titlu: ")
    autor=input("Autor: ")
    an=int(input("An: "))
    carti[i]=(titlu, autor, an)
    i+=1

print("Autori în ordine alfabetică:")
autori=[""]*n
i=0
while i<n:
    autori[i]=carti[i][1]
    i+=1

i=0
while i<n-1:
    j=i+1
    while j<n:
        if autori[i]>autori[j]:
            autori[i], autori[j]=autori[j], autori[i]
        j+=1
    i+=1

i=0
while i<n:
    if i==0 or autori[i]!=autori[i-1]:
        print(autori[i])
    i+=1

print("Autori și cărți după an:")
i=0
while i<n-1:
    j=i+1
    while j<n:
        if carti[i][2]>carti[j][2]:
            carti[i], carti[j]=carti[j], carti[i]
        j+=1
    i+=1

i=0
while i<n:
    print(carti[i][1], "-", carti[i][0], "(", carti[i][2], ")")
    i+=1

x=input("Autorul X: ")
print("Cărți ale lui", x, "după 1989:")
i=0
while i<n:
    if carti[i][1]==x and carti[i][2]>1989:
        print(carti[i][0])
    i+=1'''