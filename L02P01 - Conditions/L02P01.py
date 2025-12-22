a, b = map(int, input().split())
if (a > b):
    print(a)
else:
    print(b)
    
# ======================================    
n = int(input())

if (n > 0):
    print("Positive number")
elif (n == 0):
    print("Zero number")
else:
    print("Negative number")
    
# ======================================
a, b = map(int, input().split())
lucky_number = int(input())

if a * b == lucky_number:
  print("Both")
elif lucky_number % a == 0:
  print("Upan")
elif lucky_number % b == 0:
  print("Ipan")
else:
  print("No")

# ======================================
old, new = map(int, input().split())

used = new - old
cost = 0

if used <= 50:
  cost = used * 1484
elif used <= 100:
  cost = 50 * 1484 + (used - 50) * 1533
elif used <= 200:
  cost = 50 * 1484 + 50 * 1533 + (used - 100) * 1786
elif used <= 300:
  cost = 50 * 1484 + 50 * 1533 + 100 * 1786 + (used - 200) * 2242
elif used <= 400:
  cost = 50 * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + (used - 300) * 2503
else:
  cost = 50 * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + 100 * 2503 + (used - 400) * 2587
  
total = int(cost * 1.1)
print(total)


# ======================================
keo_1, keo_2, keo_3, keo_4 = map(int, input().split())

max = keo_1

if keo_2 > max:
  max = keo_2
  
if keo_3 > max:
  max = keo_3
  
if keo_4 > max:
  max = keo_4
  
print(max)

# ======================================

coor_friends_house = int(input())

steps = coor_friends_house // 5

remainder = coor_friends_house % 5

if remainder > 0:
    steps += 1
    
print(steps)


# ======================================

n,m,a = map(int, input().split())

horizontal = (n + a - 1) // a
vertical = (m + a - 1) // a

print(horizontal * vertical)

# ======================================
# Next Round 158A
num_players, threshold = map(int, input().split())
scores = list(map(int, input().split()))

count = 0
for s in scores:
    if s > 0 and s >= scores[threshold - 1]:
        count += 1
        
print(count)