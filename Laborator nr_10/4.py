# Задача 4. Количество гласных и согласных в слове
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

print("Consoane:", consoane_gasite, numar_consoane)