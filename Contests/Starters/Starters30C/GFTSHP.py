for t in range(int(input())):
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()

    s = 0
    ct = 0

    for i in range(n):
        if (s + (arr[i] + 1) // 2) <= k:
            ct += 1
            s += arr[i]
    
    print(ct)