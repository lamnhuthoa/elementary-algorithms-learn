# Bai 5
# Palindrome string
'''
Ipan loves palindromic strings. We all know that a string is called a palindrome if we reverse the string, we will get a string similar to the original one.

You are given a string with length N. Help Ipan check if the given string is a palindrome using recursion.

Input:
The first line is length N of string
The next line is given string containing only lowercase characters.

Output:
Print "YES" if the given string is a palindrome, otherwise print "NO"
'''
def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)

n = int(input())
s = input().strip()
if is_palindrome(s, 0, n - 1):
    print("YES")
else:
    print("NO")