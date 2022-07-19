T = int(input())
for t in range(T):
    G = int(input())
    for g in range(G):
        I, N, Q = map(int, input().strip().split())
        if N%2==0:
            print(N//2)
        else:
            if (I==Q):
                print(N//2)
            else:
                print(N//2+1)
                 