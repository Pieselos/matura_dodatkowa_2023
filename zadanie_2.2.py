


def czymniejszy(n,s,k1,k2):
    print(n,s,k1,k2)
    n=n-1
    k1=k1-1
    k2=k2-1

    i = k1
    j = k2
    while i <= n and j <= n:
        if s[i] == s[j]:
            i = i+1
            j = j+1
        else:
            if s[i]<s[j]:
                return "TAK"
            else:
                return "NIE"
    if j<= n:
        return "TAK"
    else:
        return "NIE"
plik = open('dane/DANE_M/slowa3.txt')
tekst = plik.readlines()
print(tekst)
liczby = tekst[2].strip().split(' ')
print(liczby)
print(czymniejszy(int(tekst[0].strip()),tekst[1].strip(),int(liczby[0]),int(liczby[1])))
