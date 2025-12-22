# Bai 8
# Fibonacci number
# Find the number by the index in Fibonacci sequence
import sys
sys.setrecursionlimit(10003)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))