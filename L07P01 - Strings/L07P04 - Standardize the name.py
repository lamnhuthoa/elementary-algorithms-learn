# Bai 4
# Standardize the name
num_names = int(input())

for i in range(num_names):
    full_name = input().strip()
    names = full_name.split()
    
    first_character = ''
    rest = ''
    returned_name = []
    for name in names:
        first_character = name[0:1].upper()
        rest = name[1:].lower()
        returned_name.append(first_character + rest)
        
    print(' '.join(returned_name))