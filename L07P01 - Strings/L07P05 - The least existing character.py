# Bai 5
# The least existing character
n = int(input().strip())

letters = []
for _ in range(n):
    text = input().strip()
    char_count = {}
    
    for c in text:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            upper_character = c.upper()
            if upper_character in char_count:
                char_count[upper_character] += 1
            else:
                char_count[upper_character] = 1
            
    if not char_count:
        print()
        continue
    
    min_freq = min(char_count.values())
    
    for code in range(ord('A'), ord('Z') + 1):
        letter = chr(code)
        if char_count.get(letter, 0) == min_freq:
            letters.append(letter)
            break
    
 
for letter in letters:
    print(letter)  