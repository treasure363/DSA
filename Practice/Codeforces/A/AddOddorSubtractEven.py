#https://codeforces.com/contest/1311/problem/A
for _ in range(int(input())):
    a, b = map(int, input().strip().split())
    if a < b:
        if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1):
            print(2)
        else:
            print(1)
    elif a > b:
        if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1):
            print(1)
        else:
            print(2)
    else:
        print(0)