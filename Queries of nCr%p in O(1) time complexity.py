for i in range(int(input())):
    k,n=map(int,input().split())
    l = list(map(int,input().split()))
    res = -1
    for i in range(1,n+1):
        for j in l:
            res +=(j+i)
    print(res)