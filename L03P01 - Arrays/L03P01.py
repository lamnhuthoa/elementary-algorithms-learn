### LOOP STATEMENTS ###
# ============ BAI 1 =============
total = 0
for i in range(1,6):
    print(i)
    total += i

print(total)

# ============ BAI 2 =============

data_list = []

data = int(input())

while data != 0:
    data_list.append(data)
    data = int(input())
  
count = 0
for i in data_list:
    if i == 5:
        count += 1
    
    
print(count)

# ============ BAI 3 =============
data_list = []

data = int(input())

while data != -1:
    data_list.append(data)
    data = int(input())
  
max = data_list[0]
min = data_list[0]
for i in data_list:
    if i > max:
      max = i
    
    if i < min:
      min = i
    
    
print(max, min)

# ========== BAI 4 ============
import math
num = int(input())

if num < 2: 
    print("NO")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print("YES")
    else:
        print("NO")
    
# ======== BAI 5 ==========
data_list = []

data = int(input())

while data != 0:
     data_list.append(data)
     data = int(input())

ascending = True
for i in range(len(data_list) - 1):
    if data_list[i] >= data_list[i + 1]:
        ascending = False
        break
    
if ascending:
  print("YES")
else:
  print("NO")
    

# ========= BAI 6 ==========
so_tui_keo = int(input())
data_list = []
for i in range(so_tui_keo):
  so_luong_keo = int(input())
  data_list.append(so_luong_keo)
  
equal = True
if len(data_list) == so_tui_keo:
  for i in data_list:
    if i % 2 != 0:
      equal = False
      break
      
print("YES" if equal else "NO")

# ======== BAI 7 ===========
num = int(input())

for i in range(num):
  star_string=""
  if i == 0 or i == num - 1:
    for j in range(num):
      star_string += "*"
    print(star_string)
  else:
    for j in range(num):
      if j == 0 or j == num - 1:
        star_string += "*"
      else:
        star_string += " "
    print(star_string)
    
# ======== BAI 7 short ========
num = int(input())

for i in range(num):
    if i == 0 or i == num - 1:
        print("*" * num)
    else:
        print("*" + " " * (num - 2) + "*")


# ========= CODE FORCE ===========
# TRAM 116A
stops = int(input())

min = 0
remaining_customers = 0
for stop in range(stops):
    passengers_out, passengers_in = map(int, input().split())
    remaining_customers = remaining_customers - passengers_out + passengers_in
    if remaining_customers > min:
        min = remaining_customers
        
print(min)

# Vanya and Cubs - 492A
num_cubes = int(input())
height = 0
used_cubes = 0
    
for level in range(1, num_cubes + 1):
    cubes_need = level * (level + 1) // 2
    if used_cubes + cubes_need > num_cubes:
        break

    used_cubes += cubes_need
    height += 1

print(height)

# ==== Stair, Peak, or Neither? - 1950A ====
test_cases = int(input())
for case in range(test_cases):
    a, b, c = map(int, input().split())
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")

# ==== Upscaling - 1950B ====
test_cases = int(input())
for case in range(test_cases):
    n = int(input())
    grid = []
    for i in range(n):
        row = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                row += "##"
            else:
                row += ".."
        grid.append(row)
        grid.append(row)
    print("\n".join(grid))

# ==== Little Nikita ====
tower_build_times = int(input())
for time in range(tower_build_times):
    cubes_put, cubes_removed = map(int, input().split())
    