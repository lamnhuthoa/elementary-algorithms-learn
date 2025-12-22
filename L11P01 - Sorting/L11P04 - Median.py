# Bai 4
# Median
'''
Please find the median in the given array.

Given that: Median in a array is the element with the middle value of a sorted array. 
In case number of elements is even, median is average of middle two elements.

Input Format
The first line is number of elements in array N(1 <= N <= 1000)
The next line is N integers a(i) (0 <= a(i) <= 1000)

Output Format
A single number is median of the array.
'''
def merge(L, n1, R, n2, a):
    i = j = k = 0
    while i < n1 and j < n2:
        if L[i] < R[j]:
            a[k] = L[i]
            i+=1
        else:
            a[k] = R[j]
            j+=1
        k+=1
    while i < n1:
        a[k] = L[i]
        i+=1
        k+=1
    while j < n2:
        a[k] = R[j]
        j+=1
        k+=1

def merge_sort(a, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        
        L = a[:n1]
        R = a[n1:]
        
        merge_sort(L, n1)
        merge_sort(R, n2)
        merge(L, n1, R, n2, a)
        
def find_median(a, n):
    
    merge_sort(a, n)
    
    if n % 2 == 1:
        median = a[n // 2]
    else:
        median = (a[n // 2 - 1] + a[n // 2]) / 2
        
    return median
    
    

n = int(input())
a = list(map(int, input().split()))
    
median = find_median(a, n)

print(median)