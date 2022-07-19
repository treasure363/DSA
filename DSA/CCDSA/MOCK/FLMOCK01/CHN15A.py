for t in range(int(input())):
    N, K = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    ct = 0
    for i in arr:
        if (i + K) % 7 == 0:
            ct += 1
    print(ct)