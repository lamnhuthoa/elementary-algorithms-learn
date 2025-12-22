# Merge
# Given two arrays A and B have m and n elements, respectively, arranged in non-increasing order. The array C is the sum of A and B (C = A + B)
# Requirement: Look for the smallest value k in the array C, k is calculated from 0

# Input
# The first line contains m, n, k respectively, are number of array elements A, B and kth-small elements needed to find
# 2nd line contains m integers of A
# 3rd line contains n integers of B

# Output
# Include only one integer, the value of the k-small number in array C
def merge(L, n1, R, n2, a, n):
    i = j = k = 0
    
    while (i < n1 and j < n2):
        if L[i] < R[j]:
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
        mid = n // 2
        L = a[:mid]
        R = a[mid:]
        
        merge_sort(L, len(L))
        merge_sort(R, len(R))
        merge(L, len(L), R, len(R), a, n)
        
m,n,k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
total = m + n

merge_sort(C, total)

print(C[k])