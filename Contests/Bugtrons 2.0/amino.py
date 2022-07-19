n = int(input())
a = list(map(int, input().strip().split()))
prev = a[0]
ct = 0
for i in range(1, n):
    if a[i]>prev:
        ct += 1
        print(ct, end=" ")
        prev = a[i]
        ct = 0
    else:
        ct += 1
print("0 "*(ct+1))