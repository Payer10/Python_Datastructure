def insertion_sort(l):
    n = len(l)
    for i in range(1,n):
        item = l[i]
        j = i - 1
        while j >= 0 and l[j] > item:
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = item
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    insertion_sort(arr)
    print(arr)