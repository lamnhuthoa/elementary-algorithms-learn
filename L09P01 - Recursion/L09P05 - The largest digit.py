# Bai 5
# The largest digit
import sys
sys.setrecursionlimit(10003)

n = int(input())

def get_largest_digit(n):
    if n < 0:
        n = n * (-1)
        
    if n < 10:
        return n
    
    last_digit = n % 10
    largest_in_rest = get_largest_digit(n // 10)
    
    return last_digit if last_digit > largest_in_rest else largest_in_rest
    
print(get_largest_digit(n))