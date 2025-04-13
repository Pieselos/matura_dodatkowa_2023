def iloczyn(x,y):
    if y==1:
        return x
        print(x,y)
    else:
        k = y // 2
        z = iloczyn(x,k)
        print(x,y,k,z)
        if y % 2 == 0:
            return z+z
        else:
            return x+z+z


print(iloczyn(112,112))