# Crossroads
intersections = [list(map(int, input().split())) for _ in range(4)]

accident = False
for i in range(4):
    l, s, r, p = intersections[i]
    
    if l == 1 and intersections[(i+3)%4][3] == 1:
        accident = True
    if s == 1 and intersections[(i+1)%4][3] == 1:
        accident = True
    if r == 1 and intersections[i][3] == 1:
        accident = True
        
print("YES" if accident else "NO")


# Naive
i0 = list(map(int, input().split()))
i1 = list(map(int, input().split()))
i2 = list(map(int, input().split()))
i3 = list(map(int, input().split()))

accident = (
    (i0[0] and i3[3]) or (i0[1] and i1[3]) or (i0[2] and i0[3]) or
    (i1[0] and i0[3]) or (i1[1] and i2[3]) or (i1[2] and i1[3]) or
    (i2[0] and i1[3]) or (i2[1] and i3[3]) or (i2[2] and i2[3]) or
    (i3[0] and i2[3]) or (i3[1] and i0[3]) or (i3[2] and i3[3])
)
print("YES" if accident else "NO")