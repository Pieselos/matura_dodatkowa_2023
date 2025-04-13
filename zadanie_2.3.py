def czymniejszy(n,s,k1,k2):

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
                return True
            else:
                return False
    if j<= n:
        return True
    else:
        return False

s = "kalafiorowa"
n = len(s)
tablica = []
for i in range(1,n+1):
    tablica.append(i)

print(tablica)

for i in range(0,n-1):
    for j in range(0,n-i-1):
        print(czymniejszy(n,s,tablica[j],tablica[j+1]),tablica[j],tablica[j+1])
        if czymniejszy(n,s,tablica[j+1],tablica[j]):
            tmp = tablica[j]
            tablica[j] = tablica[j+1]
            tablica[j+1] = tmp

print(tablica)