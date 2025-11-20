# Задача 5. Составление самого маленького числа
x=int(input("Введите целое и трёхзначное число: "))
s=x//100
d=(x//10)%10
e=x%10
if s<=d and s<=e:
    if d<=e:
        m=s*100+d*10+e
    else:
        m=s*100+e*10+d
elif d<=s and d<=e:
    if s<=e:
        m=d*100+s*10+e
    else:
        m=d*100+e*10+s
else:
    if s<=d:
        m=e*100+s*10+d
    else:
        m=e*100+d*10+s
print("Самое маленькое число:", m)