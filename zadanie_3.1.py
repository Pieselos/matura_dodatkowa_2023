plik = open('./dane/DANE_M/anagram.txt','r')
tekst = plik.readlines()
plik.close()

licznik_zrownowazowe = 0
licznik_prawie = 0
tab_bin = []
for i in tekst:
    tab_bin.append(i.strip())

for liczba_bin in tab_bin:
    liczba_jedynek = 0
    for char in liczba_bin:
        if char=='1':
            liczba_jedynek+=1
    liczba_zer = len(liczba_bin)-liczba_jedynek

    if liczba_zer == liczba_jedynek:
        licznik_zrownowazowe += 1
        continue
    if abs(liczba_zer-liczba_jedynek) == 1:
        licznik_prawie +=1

print(licznik_zrownowazowe,licznik_prawie)
