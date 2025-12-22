# Bai 2
# First repeating character (don't use set, most efficient run time, non-pythonic way)
def first_repeating_character(s):
    char_count = [0] * 256
    
    for char in s:
        char_count[ord(char)] += 1
        if char_count[ord(char)] == 2:
            return char
    return 'null'

s = input().strip()
result = first_repeating_character(s)
print(result)