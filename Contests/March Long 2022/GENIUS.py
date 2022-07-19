for t in range(int(input())):
    N, X = map(int, input().strip().split())
    if X==0:
        print("YES")
        print(0, 0, N)
    elif (X == 3 * N - 1 or X == 3 * N - 2 or X == 3 * N - 5):
        print("NO")
    elif X % 3 == 0:
        print("YES")
        print(X // 3, 0, N - X // 3)
    elif X % 3 == 1:
        print("YES")
        print((X + 2) // 3, 2, N - ((X + 2) // 3 + 2))
    elif X % 3 == 2:
        print("YES")
        print((X + 1) // 3, 1, N - ((X + 1) // 3 + 1))
    else:
        print("NO")
