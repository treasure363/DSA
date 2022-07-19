for t in range(int(input())):
    n = map(int, input().strip().split())
    inp = input()
    arr = [i for i in inp]
    arr.sort()
    print(''.join([str(i) for i in arr]))