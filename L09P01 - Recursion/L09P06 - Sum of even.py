# Bai 6
# Sum of even
import sys
sys.setrecursionlimit(10003)

n = int(input())
a = list(map(int, input().split()))

def sum_even(a_list):
    if not a_list:
        return 0
    if a_list[0] % 2 == 0:
        return a_list[0] + sum_even(a_list[1:])
    else:
        return sum_even(a_list[1:])
    
print(sum_even(a))