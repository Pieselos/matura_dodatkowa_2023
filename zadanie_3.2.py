plik = open('./dane/DANE_M/przyklad.txt','r')
tekst = plik.readlines()
plik.close()

tab_bin = []
for i in tekst:
    tab_bin.append(i.strip())


slownikanagram = dict()
for i in range(0,9):
    kod = i*10+8-i
    slownikanagram[kod] = []
for liczba_bin in tab_bin:
    if len(liczba_bin)!= 8:
        continue
    if liczba_bin[0]=='0':
        continue
    liczba_jedynek = 0
    for char in liczba_bin:
        if char=='1':
            liczba_jedynek+=1
    liczba_zer = len(liczba_bin)-liczba_jedynek

    kod = liczba_jedynek*10+liczba_zer
    print(kod)
    slownikanagram[kod].append(liczba_bin)
# print(slownikanagram)
kod_max = 0
lenmaks = 0

print(slownikanagram[44],slownikanagram[35],slownikanagram[53])



