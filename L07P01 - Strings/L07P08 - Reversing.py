# Bai 8
# Reversing
text = input().strip()

array_text = text.split()
reversed_list = []

for i in range(len(array_text) - 1, -1, -1):
    reversed_list.append(array_text[i])
    
print(' '.join(reversed_list))