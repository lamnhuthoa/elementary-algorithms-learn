# Bai 5
# Odd - Even Sort
'''
You are given an array. 
Please sort positions of even integers in increasing order and sort positions of odd integers in decreasing order.

Example:
First line: 4 6 1 3 2
Even positions: 4 6 X X 2
Odd positions: X X 1 3 X
Sorted: 2 4 3 1 6

Output:
A single line is N elements of array after sorting even integers in increasing order and odd integers in decreasing order.
'''
def merge(L, n1, R, n2, a, sort_type: str):
    i = j = k = 0
    while i < n1 and j < n2:
        if sort_type == 'asc':
            if L[i] < R[j]:
                a[k] = L[i]
                i+=1
            else:
                a[k] = R[j]
                j+=1
        else: # desc
            if L[i] > R[j]:
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


def merge_sort(a, n, sort_type: str):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        L = a[:n1]
        R = a[n1:]
        merge_sort(L, n1, sort_type)
        merge_sort(R, n2, sort_type)
        merge(L, n1, R, n2, a, sort_type)

def odd_even_sort(a, n):
    evens = []
    odds = []
    
    for num in a:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
            
    merge_sort(evens, len(evens), 'asc')
    merge_sort(odds, len(odds), 'desc')
    
    i_even, i_odd = 0, 0
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = evens[i_even]
            i_even += 1
        else:
            a[i] = odds[i_odd]
            i_odd += 1
    
n = int(input())
a = list(map(int, input().split()))

odd_even_sort(a, n)
    
for i in range(n):
    print(a[i], end=" ")