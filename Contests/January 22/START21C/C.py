T = int(input())
for t in range(T):
    p = list(map(int, input().strip().split()))
    N, x, y = p[0], p[1], p[2]
    if (x==y) or ((x+y)==(N+1)):#x and y in diagonal
        print(0)
    else:#not in diagonal
        if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):
            print(0)
        else:
            print(1)