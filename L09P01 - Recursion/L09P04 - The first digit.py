# Bai 4
# The first digit
import sys
sys.setrecursionlimit(10003)

number = int(input())

def get_first_digit(number):
    
    if number < 0:
        number = number * (-1)
        
    if number < 10:
        return number
    
    return get_first_digit(number // 10)

print(get_first_digit(number))