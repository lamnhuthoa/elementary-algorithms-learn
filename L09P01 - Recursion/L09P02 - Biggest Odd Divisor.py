# Bai 2
# Biggest Odd Divisor
import sys
sys.setrecursionlimit(10003)

number = int(input())

def find_biggest_divisor(number):
    if number % 2 == 1:
        return number
    return find_biggest_divisor(number // 2)


print(find_biggest_divisor(number))