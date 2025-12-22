# Bai 3
# Prime Sort
'''
Please sort the array in increasing order except prime numbers. 
This means that prime numbers stay in the same positions before sorting.

A prime number is a positive integer that can only be exactly divided by 1 and itself without leaving a remainder.

Input Format
The first line is number of elements in array N(1 <= N <= 10^3)
The next line is N integers A(i) (0 <= i < N, |A(i)| <= 10^6)

Output:
A single line is N elements of array after sorting in increasing order and prime numbers staying in the old positions.
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def merge(L, n1, R, n2, a, n):
    i = j = k = 0
    while i < n1 and j < n2:
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

'''
    a: non_primes
    n: len(non_primes)
'''
def merge_sort(a, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        L = a[:n1]
        R = a[n1:]
        merge_sort(L, n1)
        merge_sort(R, n2)
        merge(L, n1, R, n2, a, n)

def prime_sort(a, n):
    non_primes = [x for x in a if not is_prime(x)]
    
    merge_sort(non_primes, len(non_primes))
    
    j = 0
    for i in range(n):
        if not is_prime(a[i]):
            a[i] = non_primes[j]
            j += 1

n = int(input())
a = list(map(int, input().split()))
    
prime_sort(a, n)

for i in range(n):
    print(a[i], end=" ")