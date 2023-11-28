def power(x,y):
    res = 1
    while (y>0):
        if ((y&1) == 1):
            res = res * x
        y = y>>1
        x = x * x
    return res
def main():
    a=int(input())
    b=int(input())
    print(power(a,b))
main()