#Ferris Wheel
#https://cses.fi/problemset/task/1090


def lowerbound(arr, n):
    l, r = 0, len(arr) - 1
    index = -1
    while (l <= r):
        mid = (l + r) // 2
        if arr[mid] <= n:
            index = mid
            l = mid + 1
        else:
            r = mid - 1
    return index

n, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()
gondola = 0

while (len(arr) != 0):
    
    a = arr[0]
    d = x - a
    if d == 0:
        rem = [arr.pop(0)]
    else:
        rem = [arr.pop(0)]
        i = lowerbound(arr, d)
        if i != -1:
            rem.append(arr.pop(i))
    gondola += 1

print(gondola)
