n = int(input())
a = list(map(int, input().strip().split()))

d = {}
for i in a:
    try:
        d[i] += 1
    except:
        d[i] = 1
print(len(d.keys()))