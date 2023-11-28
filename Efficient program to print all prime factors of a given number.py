import math

def primefactors(n):

    while n%2==0:
        print(2,end=' ')
        n//=2
    
    for i in range(3,int(math.sqrt(n))+1,2):

        while n%i==0:
            print(int(i),end=' ')
            n//=i
    if n>2:
        print(n)
n=12
primefactors(n)