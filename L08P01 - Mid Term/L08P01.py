# Mid Term
# 1. Taxi Fare
km_went = int(input())
cost = 0 

if km_went < 2:
    cost = km_went * 15000
elif 2 <= km_went < 6:
    cost = 1 * 15000 + (km_went - 1) * 13500
else:
    cost = 1 * 15000 + 4 * 13500 + (km_went - 5) * 11000
    
if km_went >= 12:
    cost *= 0.9
    
print(int(cost))
    
# 2. Christmas Tree
num_lines = int(input())
for i in range(num_lines):
    spaces = num_lines - i - 1
    stars = 2 * i + 1
    line = " " * spaces + "*" * stars
    print(line)

# 3. Valid email
text = input()

def check_email(local_part, domain_name_part) -> bool:
    # check local_part
    for ch in local_part:
        if not (
            'A' <= ch <= 'Z' or
            'a' <= ch <= 'z' or
            '0' <= ch <= '9' or
            ch in ['.', '_']
        ):
            return False
        
    # check domain_name_part
    if '.' not in domain_name_part or '..' in domain_name_part:
        return False
    
    for ch in domain_name_part:
        if not (
            'A' <= ch <= 'Z' or
            'a' <= ch <= 'z' or
            ch == '.'
        ):
            return False
    
    return True


if text.count('@') != 1:
    print("INVALID")
else: 
    local_part, domain_name_part = text.split('@')
    
    if not local_part or not domain_name_part:
        print("INVALID")
    else:
        if check_email(local_part, domain_name_part):
            print("VALID")
        else:
            print("INVALID")


# 4. Acronym
s = input().strip()

if len(s) > 1000:
    word = input().strip()
    
words = s.split(' ')

acronym = []
for word in words:
    acronym.append(word[0].upper())
    
ans = ''.join(acronym)
print(ans)


# 5. Magnet
# Naive:
num_of_magnets = int(input())
count_group = 1  # ít nhất luôn có 1 nhóm
magnets = []

for i in range(num_of_magnets):
    magnets.append(input().strip())


for i in range(len(magnets) - 1):
    if magnets[i] != magnets[i + 1]:
        count_group += 1

print(count_group)

# 2nd approach
num_of_magnets = int(input())

count_group = 1
prev_magnet = input().strip()

for i in range(num_of_magnets - 1):
    current_magnet = input().strip()
    if current_magnet != prev_magnet:
        count_group += 1
    prev_magnet = current_magnet
    
print(count_group)


# Sudoku
sudoku = []
for i in range(9):
    row = list(map(int, input().split()))
    sudoku.append(row)
    
is_valid = True 

# check rows and columns
for i in range(9):
    row_set = set()
    col_set = set()
    for j in range(9):
        row = sudoku[i][j]
        col = sudoku[j][i]
        if row in row_set or col in col_set:
            is_valid = False
            break
        row_set.add(row)
        col_set.add(col)
    if not is_valid:
        break
        
    
# Check 3x3 boxes
if is_valid:
    for box in range(9):  # box index 0..8
        seen = set()
        for cell in range(9):  # cell index 0..8
            box_row_index = (box // 3) * 3 + (cell // 3)
            box_col_index = (box % 3) * 3 + (cell % 3)
            cell_value = sudoku[box_row_index][box_col_index]
            if cell_value in seen:
                is_valid = False
                break
            seen.add(cell_value)
        if not is_valid:
            break
        
print("YES" if is_valid else "NO")

# Another approach
def read_grid():
    sudoku = []
    for _ in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)
        
    return sudoku

def check9(nums):
    cnt = [0] * 10
    for v in nums:
        cnt[v] += 1
        if cnt[v] > 1:
            return False
    return True

def check_rows(g):
    for i in range(9):
        if not check9(g[i]):
            return False
    return True

def check_cols(g):
    for i in range(9):
        col = []
        for j in range(9):
            col.append(g[j][i])
            
        if not check9(col):
            return False
        
    return True

def check_boxes(g):
    for bi in range(3):
        for bj in range(3):
            nums = []
            for i in range(bi * 3, bi * 3 + 3):
                for j in range(bj * 3, bj * 3 + 3):
                    nums.append(g[i][j])
                    
            if not check9(nums):
                return False
    return True
    
def check_grid(g):
    return check_rows(g) and check_cols(g) and check_boxes(g)
    
g = read_grid()
print("YES" if check_grid(g) else "NO")

    
# i: box index => box 0 -> box 8
# j: box cell index => box cell 0 -> box cell 8

# Sudoku 9 boxes
'''  i = 5
        0   1   2
        ---------
0 -- 0 | 1 | 2
1 -- 3 | 4 | 5 <-- box: row 1, column 2 (5 // 3 == 1, 5 % 3 == 2)
2 -- 6 | 7 | 8
'''

# Inside Box => Cells
'''  j = 4
        0   1   2
        ---------
0 -- 0 | 1 | 2
1 -- 3 | 4 | 5 <-- cell: row 1, column 1 (4 // 3 == 1, 4 % 3 == 1)
2 -- 6 | 7 | 8
'''

# box index => [i // 3][i % 3]
# cell index => [j // 3][j % 3] 


# In Sudoku Board
'''
        0 1 2 3 4 5 6 7 8
        -----------------
0 -- 5 3 4 6 7 8 9 1 2
1 -- 6 7 2 1 9 5 3 4 8
2 -- 1 9 8 3 4 2 5 6 7
3 -- 8 5 9 7 6 1 4 2 3
4 -- 4 2 6 8 5 3 7 9 1
5 -- 7 1 3 9 2 4 8 5 6
6 -- 9 6 1 5 3 7 2 8 4
7 -- 2 8 7 4 1 9 6 3 5
8 -- 3 4 5 2 8 6 1 7 9
'''

# row: 1 * 3 + 1 = 4
# column: 2 * 3 + 1 = 7
# sudoku[4][7] = 9