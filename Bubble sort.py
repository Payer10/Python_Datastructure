def Bubble_sort(l):
    n = len(l)
    for i in range(0,n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    Bubble_sort(arr)
    print(arr)