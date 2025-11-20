# Задача 12. Сумма цифр двухзначных чисел
n=int(input("Введите сумму цифр: "))
numar=10
while numar<=99:
    cifra1=numar//10     
    cifra2=numar%10     
    suma_cifre=cifra1+cifra2  
    
    if suma_cifre==n:       
        print(numar)   
    numar=numar+1