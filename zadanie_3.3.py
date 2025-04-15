plik = open('dane/DANE_M/anagram.txt')
tekst = plik.readlines()
plik.close()

tab_int = []

for i in tekst:
    tab_int.append(int(i.strip(),2))

najwieksza_roznica = abs(tab_int[0]-tab_int[1])
for i in range(0,len(tab_int)-1):
    roznica = abs(tab_int[i]-tab_int[i+1])
    if roznica > najwieksza_roznica:
        najwieksza_roznica = roznica

print(bin(najwieksza_roznica)[2:])




