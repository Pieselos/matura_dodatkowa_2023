def rot13(slowo):
    szyfrowane = ''
    for char in slowo:
        nr = ord(char)
        nr += 13
        if nr > ord('z'):
            nr -= 26
        szyfrowane += chr(nr)
    return szyfrowane
print(rot13('aren'))