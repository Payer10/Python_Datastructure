def catalan(n):
    if n<=1:
        return 1
    res = 1
    for i in range(1,n+1):
        res *= (4*i -2)
        res //= (i+1)
    return res
print(catalan(int(input())))
