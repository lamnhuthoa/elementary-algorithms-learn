s = list(input().strip())
a = [s[i] if i % 2 == 0 else "_" for i in range(len(s))]
b = [s[i] if i % 2 != 0 else "_" for i in range(len(s))][::-1]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == "_" and b[j] != "_":
            a[i] = b[j]
            b[j] = "_"
            break
            
print(a)

# Advanced:
# s = list(input().strip())
# even_list = [s[i] for i in range(0, len(s), 2)]
# odd_list = [s[i] for i in range(1, len(s), 2)][::-1]

# ans = []
# ei = oi = 0

# for i in range(len(s)):
#     if i % 2 == 0:
#         ans.append(even_list[ei])
#         ei += 1
#     else:
#         ans.append(odd_list[oi])
#         oi += 1
            
# print("".join(ans))