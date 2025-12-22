# Bai 3
# Find element
'''
You are given an increasing array with N elements and an integer x, 
find the apprearance position of x in array (index begins with 1)

Input:
The first line contains number of elements in array N and number needed to find position x
The next line is N integers sorted in increasing order

Output:
Print the appearance position of x (index begin with 1) in array. If cannot find x, print -1
'''
import sys
sys.setrecursionlimit(10003)
def find_element(a, n, x):
    if n == 0:
        return -1
    
    if a[0] == x:
        return 1
    
    res = find_element(a[1:], n - 1, x)
    if res == -1:
        return -1
    else:
        return res + 1

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(find_element(a, n, x))

def find_element(a, n, x):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(find_element(a, n, x))