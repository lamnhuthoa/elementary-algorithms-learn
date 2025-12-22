# ===== Bai 1 =====
m, n = map(int, input().split())

rows = [list(map(int, input().split())) for _ in range(m)]
sums = [sum(row) for row in rows]
    
for i, total in enumerate(sums):
    print(f"{i}: {total}")


# ===== Bai 2 =====
m, n = map(int, input().split())

a = []
for i in range(m):
  temp = list(map(int, input().split()))
  a.append(temp)

negative_columns = []

for j in range(n):
  all_negative = True
  for i in range(m):
    if a[i][j] >= 0:
      all_negative = False
      break
  
  if all_negative:
    negative_columns.append(j)
    
    
print(*negative_columns)

# ===== Bai 3 =====
# Prime numbers on the border
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


m, n = map(int, input().split())

a = []

for i in range(m):
    temp = list(map(int, input().split()))
    a.append(temp)
    

count = 0

for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            if is_prime(a[i][j]):
                count = count + 1
                
                
print(count)

# ===== Bai 4 =====
# Prime numbers on the main diagonal
def is_prime(x):
  if x < 2:
    return False
  
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      return False
  return True

n = int(input())
a = []
for i in range(n):
  temp = list(map(int, input().split()))
  a.append(temp)
  
count = 0
for i in range(n):
  for j in range(n):
    if i == j:
      if is_prime(a[i][j]):
        count += 1
        
print(count)


# ===== Bai 5 =====
# Product of primes on secondary diagonal
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

MOD = 1_000_003
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

product = 1
found_prime = False

for i in range(n):
    j = n - 1 - i
    if is_prime(a[i][j]):
        product = (product * a[i][j]) % MOD
        found_prime = True
        
        
if not found_prime:
    print(1)
else:
    print(product)

# ===== Bai 6 =====
# Row with most even numbers
m, n = map(int, input().split())
a = []
for i in range(m):
  temp = list(map(int, input().split()))
  a.append(temp)
  
max_even_count = 0
row_index = -1

for i in range(m):
    even_count = 0
    for j in range(n):
        if a[i][j] % 2 == 0:
            even_count += 1
        
    if even_count > max_even_count:
        max_even_count = even_count
        row_index = i

print(row_index)

# ===== Bai 7 =====
# Count images
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

photo_over_hundred_likes = 0
  
for i in range(m):
  for j in range(n):
    if a[i][j] > 100:
      photo_over_hundred_likes += 1
      
print(photo_over_hundred_likes)

# ===== Bai 8 =====
# Count Queens
# Count "queen" values in a square matrix. A value is considered as a queen when it is the largest number in the row, 
# the column and 2 diagonals passing through it.

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

max_in_row = [max(row) for row in a]
max_in_col = [max(a[r][c] for r in range(n)) for c in range(n)]

max_main_diagonal = {}
max_secondary_diagonal = {}

for i in range(n):
    for j in range(n):
        d1 = i - j
        d2 = i + j
        if d1 not in max_main_diagonal or a[i][j] > max_main_diagonal[d1]:
            max_main_diagonal[d1] = a[i][j]
        if d2 not in max_secondary_diagonal or a[i][j] > max_secondary_diagonal[d2]:
            max_secondary_diagonal[d2] = a[i][j]
            
queen_count = 0
for i in range(n):
    for j in range(n):
        value = a[i][j]
        if (value == max_in_row[i] and
            value == max_in_col[j] and
            value == max_main_diagonal[i - j] and
            value == max_secondary_diagonal[i + j]):
            queen_count += 1
            
print(queen_count)

# ===== Bai 9 =====
# Saddle values
# Count "saddle" value in a matrix. A value is considered as "saddle" when it is largest in the row and smallest in the column.
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

max_in_row = [max(row) for row in a]
min_in_col = [min(a[r][c] for r in range(m)) for c in range(n)]

saddle_count = 0
for i in range(m):
    for j in range(n):
        value = a[i][j]
        if value == max_in_row[i] and value == min_in_col[j]:
            saddle_count += 1
        
print(saddle_count)

# ===== Bai 10 =====
# Create matrix
# Given 2 initial values of the matrix and a number p
# create a matrix with 2 initial values, known that the following value is equal to the remainder of sum of 2 preceding values divided by p
# noted that left to right and top to bottom.

m, n = map(int, input().split())
a, b, p = map(int, input().split())

matrix = [[0]*n for _ in range(m)]

flat = [a, b]

for _ in range(m * n - 2):
    flat.append((flat[-1] + flat[-2]) % p)

matrix = [flat[i*n:(i+1)*n] for i in range(m)]

for row in matrix:
    print(*row)