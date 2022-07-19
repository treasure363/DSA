T = int(input())
arr = []
for t in range(T):
    arr.append(int(input()))
arr.sort()
dp = []
for i in range(len(arr)):
    dp.append(arr[i]*(len(arr)-i))
print(max(dp))