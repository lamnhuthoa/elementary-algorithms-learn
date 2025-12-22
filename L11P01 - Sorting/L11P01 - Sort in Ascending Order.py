# Bai 1
# Sort in Ascending Order
def insert_asc(a, n, x):
    j = n
    while j > 0:
        if (a[j-1] <= x):
            break
        a[j] = a[j - 1]
        j -= 1
    a[j] = x
    
    
def insertion_sort(a):
    for i in range(1, len(a), 1):
        x = a[i]
        insert_asc(a, i, x)
        
        
n = int(input()) # 4
a = list(map(int, input().split())) # 2 10 9 8

insertion_sort(a)

for i in range(n):
    print(a[i], end=" ")