arr = [1,2,4,8,16,32,64,128,256,512,1024,2048]
arr.sort(reverse=True)


def r(n):
    for i in arr:
        if i <= n:
            return 1 + r(n-i)
    return 0

for i in range(int(input())):
    print(r(int(input())))