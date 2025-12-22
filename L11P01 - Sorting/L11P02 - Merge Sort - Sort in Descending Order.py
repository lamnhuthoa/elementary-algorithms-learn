    
# Merge Sort (Descending Order)
def merge(L, n1, R, n2, a, n):
    i = j = k = 0
    
    while (i < n1 and j < n2):
        if L[i] > R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    while (i < n1):
        a[k] = L[i]
        i += 1
        k += 1
    while (j < n2):
        a[k] = R[j]
        j += 1
        k += 1
    
    
def merge_sort(a, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        L = a[:n1]
        R = a[n1:]
        
        merge_sort(L, n1)
        merge_sort(R, n2)
        merge(L, n1, R, n2, a, n)
        
n = int(input())
a = list(map(int, input().split()))

merge_sort(a, n)

for i in range(n):
    print(a[i], end=" ")