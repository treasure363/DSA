T = int(input())
for t in range(T):
    N, X, Y = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    c, f = 0, 0
    for i in range(N):
        temp = B[i]-A[i]
        if temp%X==0:
            c = temp//X
        elif temp%Y==0:
            c = temp//Y
        else:
            c = None
            break
    if c==None:
        print("No")
    else:
        for i in range(N):
            temp = B[i]-A[i]
            if not(temp==(c*X) or temp==(c*Y)):
                f = 1
        if f==0:
            print("Yes")
        else:
            print("No")