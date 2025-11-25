'''# Задача 4. Количество гласных и согласных в слове
text=input("Introduceți textul: ")

vocale="aeiouAEIOU"
consoane="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vocale_gasite=""
numar_vocale=0

i=0
while i<len(text):
    if text[i] in vocale:
        vocale_gasite=vocale_gasite+text[i]
        numar_vocale=numar_vocale+1
    i=i+1

print("Vocale:", vocale_gasite, numar_vocale)

consoane_gasite=""
numar_consoane=0

i=0
while i<len(text):
    if text[i] in consoane:
        consoane_gasite=consoane_gasite+text[i]
        numar_consoane=numar_consoane+1
    i=i+1

print("Consoane:", consoane_gasite, numar_consoane)'''



'''# Задача 5. Исключение строки из введённого текста 
text=input("Introduceți textul: ")
sc=input("Introduceți șirul de eliminat: ")

i=0
rezultat=""

while i<len(text):
    if text[i:i+len(sc)]==sc:
        i=i+len(sc)
    else:
        rezultat=rezultat+text[i]
        i=i+1

print("Textul fără șirul", sc+ ":", rezultat)'''



'''# Задача 6. Текст палиндром
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
    print("Textul NU este palindrom")'''