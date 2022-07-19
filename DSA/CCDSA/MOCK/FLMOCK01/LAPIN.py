def dup(a):
    d = {}
    for i in a:
        try:
            d[i] += 1
        except:
            d[i] = 1 
    return d

for t in range(int(input())):
    s = input()
    k = len(s)//2
    l = s[:k]
    if len(s)%2==0:
        r = s[k:]
    else:
        r = s[k+1:]
    l, r = dup(l), dup(r)
    if l==r:
        print("YES")
    else:
        print("NO")