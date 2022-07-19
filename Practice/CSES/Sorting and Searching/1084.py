n, m, k = map(int, input().strip().split())
N = list(map(int, input().strip().split()))
M = list(map(int, input().strip().split()))
N.sort()
M.sort()
i, j = 0, 0
ct = 0

while(i < n):
    while(j<m and M[j] < N[i] - k):
        j += 1
    if (j<m and abs(M[j]-N[i]) <= k):
        ct += 1
        j += 1
        i += 1
    else:
        i += 1

print(ct)
