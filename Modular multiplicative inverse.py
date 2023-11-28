def ModInverse(a,m):
    for i in range(1,m):
        if(((a%m)*(i%m))%m==1):
            return i
    return -1
a=int(input())
m=int(input())
print(ModInverse(a,m))