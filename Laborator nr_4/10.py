# Задача 10.
n=int(input("Введите число: "))
suma_divizori=0
i=1
while i<n:
    if n%i==0:
        suma_divizori=suma_divizori+i
    i=i+1

if suma_divizori==n:
    print(n, "- идеальное число")
else:
    print(n, "- не идеальное число")