
def primefactor(n):
    least_prime=[0]*(n+1)
    least_prime[1]=1
    for i in range(2,n+1):
        if least_prime[i]==0:
            least_prime[i]=i
            for j in range(i*i,n+1,i):
                if least_prime[j]==0:
                    least_prime[j]=i
    for i in range(1,n+1):
        print('least prime factor or numbers',i,':',least_prime[i])
n=10
primefactor(n)
 
 