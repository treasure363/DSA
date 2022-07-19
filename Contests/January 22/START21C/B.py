T = int(input())
for t in range(T):
    p = list(map(int, input().strip().split()))
    N, M = p[0], p[1]
    n, m = 0, 0
    if M%2==0:
        m = int(M/2)
    else:
        m = int(M/2) + 1
    if N%2==0:
        n = int(N/2)
    else:
        n = int(N/2) + 1
    print(n*m)