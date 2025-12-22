# Recursion
# 5! = 1 * 2 * 3 * 4 * 5
# f(5) = 1 * 2 * 3 * 4 * 5
# f(5) = 4! * 5
# f(5) = f(4) * 5
import sys
sys.setrecursionlimit(10003)

'''
    - Recursionlimit là kích thước của callstack
    - Recursionlimit mặc định, trong Python, là 1000
    - Tham khảo hàm sys.getrecursionlimit()
'''

def factorial(number):
    if number == 1 or number == 0:
        return 1

    return number * factorial(number - 1)

total = factorial(5)
print(total)

# Stack
# Stack is a data structure, LIFO (Last in first out)