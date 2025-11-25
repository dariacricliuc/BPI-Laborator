# Задача 6. Текст палиндром
text=input("Introduceți textul: ")

i=0
j=len(text)-1
palindrom=True

while i<j:
    if text[i]!=text[j]:
        palindrom=False
        break
    i=i+1
    j=j-1

if palindrom:
    print("Textul este palindrom")
else:
    print("Textul NU este palindrom")