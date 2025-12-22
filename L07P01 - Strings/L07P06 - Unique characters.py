# Bai 6
# Unique characters
text = input().strip()

seen = []

for c in text:
    if c not in seen:
        seen.append(c)
    
print(len(seen))
