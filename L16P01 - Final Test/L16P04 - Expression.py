a = int(input())
b = int(input())
c = int(input())

results = [
    a + b + c,
    a * b + c,
    a + b * c,
    (a + b) * c,
    a * (b + c),
    a * b * c
]

max = results[0]
for item in results:
    if item > max:
        max = item
        
        
print(max)