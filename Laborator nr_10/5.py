# Задача 5. Исключение строки из введённого текста 
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

print("Textul fără șirul", sc+ ":", rezultat)