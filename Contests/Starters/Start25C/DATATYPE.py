T = int(input())
for t in range(T):
    N, X = map(int, input().strip().split())
    if N<X:
        while(N<X):
            X=X-N-1
        print(X)
    else:
        print(X)
    