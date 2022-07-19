T = int(input())
for t in range(T):
    X, Y = map(int, input().strip().split())
    print(min(X//2, Y))