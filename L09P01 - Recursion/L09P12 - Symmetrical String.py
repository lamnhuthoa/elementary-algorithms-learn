# Bai 12
# Symmetrical string
'''
Given a string s has n characters, includes uppercases, lowercases and numbers. Determine whether s is a palindrome or not.
A string is a palindrome if the string read from left to right is equal to the string read from right to left.

Input
The first line contains a positive integer n
The second line contains a string s

Output:
If s is a palindrome, print "YES", otherwise print "NO"

'''
import sys
sys.setrecursionlimit(10003)

n = int(input())
s = input().strip()

def is_palindrome_recursive(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
  
print("YES" if is_palindrome_recursive(s) else "NO")