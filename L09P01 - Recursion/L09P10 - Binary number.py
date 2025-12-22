# Bai 10
# Bỉnary Number
'''
Given a decimal number n, write a program to convert n into equivalent binary number.
Input Format: The only line of input contains a non-negative integer n
Output: In the only line print n in binary
'''
import sys
sys.setrecursionlimit(10003)

n = int(input())

def decimal_to_binary(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(n))