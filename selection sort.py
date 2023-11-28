def selection_sort(l):
    n = len(l)
    for i in range(0,n-1):
        min_ = i
        for j in range(i+1,n):
            if l[j] < l[min_]:
                min_ = j
        if min_ != i:
            temp = l[i]
            l[i] = l[min_]
            l[min_]= temp
if __name__ == "__main__":
    l = [6,3,5,2,4]
    selection_sort(l)
    print(l)