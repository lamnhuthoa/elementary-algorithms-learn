# Bai 3
# The number of digits
import sys
sys.setrecursionlimit(10003)

number = int(input())

def count_number_of_digits(number):
    if number < 0:
        number = number * (-1)
    if number < 10:
        return 1
    return 1 + count_number_of_digits(number // 10)

print(count_number_of_digits(number))
