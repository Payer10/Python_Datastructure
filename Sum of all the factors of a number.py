import math

def sumprime(n):
    if n==1:
        return 1
    result = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            if i==(n//i):
                result += i
            else:
                result += (i+n//i)
    return result+n+1

n=30
print(sumprime(n))