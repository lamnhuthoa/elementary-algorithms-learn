# ===== Bai 4 =====
num = int(input())
likes = list(map(int, input().split()))

def check_no_liked_post(likes) -> bool:
  for like in likes:
    if like == 0:
      return False
  return True
    
print("YES") if check_no_liked_post(likes) else print("NO")


# ===== Bai 5 =====
def is_prime(num) -> bool:
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

  
num = int(input())
num_list = list(map(int, input().split()))
count = 0

for item in num_list:
  if is_prime(item):
    count += 1
  
  
print(count)
    
    
# ===== Bai 6 =====
num_vase = int(input())
heights = list(map(int, input().split()))

min_height = heights[0]

for height in heights:
  if height < min_height:
    min_height = height

min_energy = 0
for h in heights:
#   while h > min_height: # Cách này tiêu tốn nhiều tài nguyên
#     h -= 1
#     min_energy += 1
    min_energy += h - min_height
    
print(min_energy)


# ==== Bai 7 ====
num = int(input())
people_list = list(map(int, input().split()))
num_male = 0
num_female = 0

for people in people_list:
  if people == 0:
    num_male += 1
  else:
    num_female += 1

if num_male == num_female:
  print("YES")
else:
  print("NO")

# ==== Bai 8 ====
def found_max_in_list(list_number):
    max_number = list_number[0]
    for num in list_number:
        if num > max_number:
            max_number = num
            
    return max_number

num = int(input())
id_number_list = list(map(int, input().split()))
id_number_list.sort()

min_id_missing = -1

if id_number_list[0] > 1:
    min_id_missing = 1
else:
    for i in range(len(id_number_list) - 1):
        if id_number_list[i + 1] - id_number_list[i] > 1:
            min_id_missing = id_number_list[i] + 1
            break


if min_id_missing == -1:
    max_id_number = found_max_in_list(id_number_list)
    min_id_missing = max_id_number + 1
    
    
print(min_id_missing)

# ==== Bai 9 ====
num_basket = int(input())
baskets_list = []
for basket in range(num_basket):
  baskets_list.append(list(map(int, input().split())))
  
# baskets_list [[2, 3], [1, 4], [2, 5]]
max_apples = baskets_list[0][0]
max_oranges = baskets_list[0][1]
chosen_index = 0

for i in range(1, len(baskets_list)):
    apples, oranges = baskets_list[i]

    # Nếu giỏ có nhiều táo hơn -> chọn luôn
    if apples > max_apples:
        max_apples = apples
        max_oranges = oranges
        chosen_index = i

    # Nếu số táo bằng nhau -> so số cam
    elif apples == max_apples and oranges > max_oranges:
        max_oranges = oranges
        chosen_index = i

# In ra chỉ số giỏ (đánh số từ 1 theo đề bài)
print(chosen_index + 1)

# ===== Bai 10 =====
n = int(input())
a = list(map(int, input().split()))

# sections = [0, 0, 0, 1, 1]

def check_lala():
    if a[-1] == 0:
        return False
    for i in range(n - 3):
    # if a[i] + a[i + 1] + a[i + 2] + a[i + 3] == 0:
        if sum(a[i:i+4]) == 0:
            return False
    return True

print('YES' if check_lala() else 'NO')


# =================
num = int(input())
id_number_list = list(map(int, input().split()))
id_number_list.sort()

frequency = [0] * 100001

for i in id_number_list:
  frequency[i] += 1
  
  
min_id_missing = 0
max_id = max(id_number_list)

for i in range(1, max_id + 2):
    if frequency[i] == 0:
        min_id_missing = i
        break

print(min_id_missing)


# ==============================
# List Comprehension
number = [1,2,3,4,5,6]
even_numbers = [x for x in number if x % 2 == 0]
print(even_numbers)
labels = ["Even" if x % 2 == 0 else "Odd" for x in number ]
print(labels)
