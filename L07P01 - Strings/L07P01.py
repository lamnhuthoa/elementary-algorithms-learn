# String and Characters
# Bai 1
# Check characters' appearance
text = input()
characters = ['b','i','g','o']

found = False

for c in text:
    if c.lower() in characters:
        found = True
        

print("YES" if found else "NO")    

# Code Forces
# New Palindrome - https://codeforces.com/problemset/problem/1832/A
t = int(input())
a = []
for _ in range(t):
    s = input().strip()
    a.append(s)
    
for item in a:
    # all same -> NO
    if len(set(item)) == 1:
        print("NO")
        continue

    # build frequency
    freq = {}
    for ch in item:
        freq[ch] = freq.get(ch, 0) + 1

    half_chars = []
    for ch, cnt in freq.items():
        half_chars.extend([ch] * (cnt // 2))

    if len(half_chars) == 0 or len(set(half_chars)) <= 1:
        print("NO")
    else:
        print("YES")
        
# Other approach
'''
🎯 Ý tưởng cực ngắn

Vì s đã là palindrome, muốn tạo một palindrome khác, ta cần ít nhất hai ký tự khác nhau xuất hiện ở phần nửa đầu.
=> Nếu chỉ có một loại ký tự duy nhất, hoặc nửa đầu toàn một ký tự giống nhau => NO.
=> Ngược lại => YES.
'''
t = int(input())

for _ in range(t):
    s = input().strip()

    # Trường hợp toàn 1 ký tự => không thể đổi
    if len(set(s)) == 1:
        print("NO")
        continue

    n = len(s)
    half = s[:n // 2]  # lấy nửa đầu

    # Nếu nửa đầu chỉ chứa 1 ký tự duy nhất => không thể tạo khác
    if len(set(half)) == 1:
        print("NO")
    else:
        print("YES")