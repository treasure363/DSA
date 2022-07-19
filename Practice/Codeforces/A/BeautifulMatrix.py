p = []
r, c = 0, 0
for i in range(5):
    # print(r, c)
    a = list(input().strip().split())
    for j in range(5):
        if a[j] == '1':
            r, c = i, j
    p.append(a)
# print(r, c)
r, c = abs(r - 2), abs(c - 2)
print(r + c)
