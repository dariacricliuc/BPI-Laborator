# Задача 11. Разница цифр в квадрате
numar = 100
while numar<=999:
    primele_doua=numar//10
    ultima=numar%10  
    diferenta=primele_doua*primele_doua-ultima*ultima
    
    if diferenta==numar:
        print(primele_doua, "*", primele_doua, "-", ultima, "*", ultima, "=", numar)
    numar=numar+1