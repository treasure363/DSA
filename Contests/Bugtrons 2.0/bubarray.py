n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
ct, d = 0, {}
m = n-k+1 if n%2 != 0 else n-k
while(m<=n):
    for i in range(0, n-m+1):
        p = arr[i:i+m]
        odd = 0
        try:
            d[str(p)] = d[str(p[-1:])] + (1 if p[-1]%2==1 else 0)
        except:
            for j in p:
                if(j%2==1):
                    odd += 1
            d[str(p)] = odd
        if(d[str(p)] == k):
            ct += 1
        #print(d)
        #print(p, odd, ct)
    m += 1
print(ct)
