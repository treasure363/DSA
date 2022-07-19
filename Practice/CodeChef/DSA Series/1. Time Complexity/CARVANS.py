# cook your dish here
import sys

T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k, min = 0, sys.maxsize
    for i in range(n):
        if arr[i]<=min:
            min = arr[i]
            k += 1
    print(k)
        