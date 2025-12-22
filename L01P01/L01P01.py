number = int(input())
digit1 = (number // 10000) % 10
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = (number // 1) % 10
total = digit1 + digit2 + digit3 + digit4 + digit5
result = total % 10
print(result)


weight = int(input())

if weight > 2 and weight % 2 == 0:
    print("YES")
else:
    print("NO")