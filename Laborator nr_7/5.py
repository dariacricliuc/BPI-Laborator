# Задача 5. Палиндромы 
def PALINDROM(n):
    original=n
    invers=0
    while n>0:
        cifra=n%10
        invers=invers*10+cifra
        n=n//10
    return original==invers

numar=100

while numar<=300:
    if PALINDROM(numar):
        patrat=numar*numar
        if PALINDROM(patrat):
            print(numar)
    numar+=1