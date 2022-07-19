for t in range(int(input())):
    N, K = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    print(abs(sum(arr[:min(K, N-K)]) - sum(arr[min(K, N-K):])))