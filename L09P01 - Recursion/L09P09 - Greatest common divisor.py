# Bai 9
# Greatest common divisor
# Write a program to find the greatest common divisor of two positive integers a and b using recursion.
# Hint: Use Euclidean algorithm.
# Input Format: A single line contains two positive integers a, b
# Output Format: In a single line print the greatest common divisor of a and b
import sys
sys.setrecursionlimit(10003)

a, b = map(int, input().split())

def find_greatest_common_divisor(a, b):
    if b == 0:
        return a
    return find_greatest_common_divisor(b, a % b)

print(find_greatest_common_divisor(a,b))