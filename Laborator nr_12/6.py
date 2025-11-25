# Задача 6. Данные о библиотеке
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
    i+=1