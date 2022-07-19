for t in range(int(input())):
    n, x, k = map(int, input().strip().split())
    total = n * x
    if k<x:
        print(0)
    elif k>total:
        print(n)
    else:
        print(total//k)