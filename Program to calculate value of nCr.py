'''
def fact(n):
    res = 1
    if n == 0:
        return 1
    for i in range(2,n+1):
        res *= i
    return res
def nCr(n, r):
    return ((fact(n)//(fact(r)*fact(n-r))))
n,r=map(int,input().split())
print(nCr(n,r))
'''
'''n=int(input())
r=int(input())
sum = 1
for i in range(1,r+1):
    sum = sum * (n - r + i) // i
print(sum)'''
from math import *

def PrintNcR(n,r):
    p = 1
    k = 1
    if n - r < r:
        r = n - r
    if r != 0:
        while r:
            p *= n
            k *= r

            m = gcd(p , k)
            p //= m
            k //= m

            n -= 1
            r -= 1
    else:
        p = 1
    return p

n = int(input())
r = int(input())
print(PrintNcR(n,r))