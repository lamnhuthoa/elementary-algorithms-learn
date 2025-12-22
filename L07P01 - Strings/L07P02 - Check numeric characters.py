# Bai 2
# Check numeric characters
text = input().split()

count_numeric_char = 0

for word in text:
    for c in word:
        if 48 <= ord(c) <= 57:
            count_numeric_char += 1
            
print(count_numeric_char)

# Cach 2
text = input()
count_numeric_char = sum(c.isdigit() for c in text)
print(count_numeric_char)