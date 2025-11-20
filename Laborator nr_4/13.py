# Задача 13. Четырёхзначное число
numar=1000
while numar<=9999:
    mii=numar//1000
    sute=(numar//100)%10
    zeci=(numar//10)%10
    unitati=numar%10  
    
    if (mii==3) and (zeci==2) and (numar%9==0):
        print(numar)
    else:
        print("Число не соответсвует установленным правилам")
    numar=numar+1