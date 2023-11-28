for i in range(int(input())):
    x,k = map(int,input().split())
    while sum(map(int,(str(x)))) %k:
        x += 1
    print(x)