# Задача 4. Данные работников одной фирмы
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
print("Salariul mediu:", medie)