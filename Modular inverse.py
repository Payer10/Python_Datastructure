def modular_inverse(a,m):
    for i in range(1,m):
        if((a%m)*(i%m)%m==1):
            return i
    return -1
if __name__ == "__main__":
    a=10
    m=17
    print(modular_inverse(a,m))
