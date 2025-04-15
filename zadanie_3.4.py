plik = open('dane/DANE_M/anagram.txt')
tekst = plik.readlines()
plik.close()

tab_int = []

for i in tekst:
    tab_int.append(int(i.strip(),2))

tab_tekst = []
for i in tab_int:
    tab_tekst.append(str(i))

# print(tab_tekst)

licznik_bez_zer = 0

for i in tab_tekst:
    if '0' not in i:
        licznik_bez_zer+=1

print(licznik_bez_zer)
# print(tab_tekst)
najwieksza_suma = 0
najwieksza_suma_liczba = None
for i in tab_tekst:
    zbiortmp = set()

    for char in i:
        zbiortmp.add(int(char))
    # print(zbiortmp)
    suma = 0
    for cyfra in zbiortmp:
        suma+=cyfra
    if suma > najwieksza_suma:
        najwieksza_suma=suma
        najwieksza_suma_liczba = int(i)


print(najwieksza_suma_liczba)