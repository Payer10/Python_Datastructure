n=int(input())
prime=[]
for i in range(n+1):
    prime.append(i)
prime[0]=0
prime[1]=0
p=2
while p*p<=n:
    if p!=0:
        for i in range(p*p,n+1,p):
            prime[i]=0
    p+=1
print(n)
for i in range(len(prime)):
    if prime[i]!=0:
        print(prime[i],end=' ')
        