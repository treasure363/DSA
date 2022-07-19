T = int(input())
for t in range(T):
    p = list(map(int, input().strip().split()))
    Z, Y, a, b, c = p[0], p[1], p[2], p[3], p[4]
    s = a+b+c
    if (Z-Y)>=s:
        print("YES")
    else:
        print("NO")