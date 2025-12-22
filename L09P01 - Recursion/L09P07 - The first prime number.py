# Bai 7
# The first prime number
import sys
sys.setrecursionlimit(10003)

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True


n = int(input())
a = list(map(int, input().split()))

def find_first_prime_number(a_list, index = 0):
    if index == len(a_list):
        return -1
    
    if is_prime(a_list[index]):
        return index
    return find_first_prime_number(a_list, index + 1)
    
    
print(find_first_prime_number(a))