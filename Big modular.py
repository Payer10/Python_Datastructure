def mod(num,a):
    res=0
    for i in range(0,len(num)):
        res=(res*10 + int(num[i]))%a
    return res
num='12316767678678'
print(mod(num,12))
