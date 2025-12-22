# Bai 11
# Hexadecimal number
'''
Given a decimal number n, write a program to convert n into equivalent hexadecimal number.

The conversion is the same as for a binary number, 
but the remainder values of 10 or more will be the 
corresponding letter starting from 'A': 10 ('A'), 11 ('B'), 12 ('C') , 13 ('D'), 14 ('E'), 15 ('F').

Input Format
The only line of input contains a non-negative integer n
Output
In the only line print n in hexadecimal
'''
import sys
sys.setrecursionlimit(10003)

n = int(input())
def decimal_to_hexadecimal(n):
    if n == 0:
        return '0'
    if n < 16:
        if n < 10:
            return str(n)
        else:
            return chr(ord('A') + n - 10)
    remainder = n % 16
    quotient = n // 16
    return decimal_to_hexadecimal(quotient) + decimal_to_hexadecimal(remainder)

print(decimal_to_hexadecimal(n))