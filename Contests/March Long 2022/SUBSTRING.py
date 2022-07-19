for t in range(int(input())):
    s = input()
    if len(s) <= 2:
        print(-1)
        continue
    arr = []
    for i in s:
        if i == s[0] or i == s[-1]:
            arr.append(False)
        else:
            arr.append(True)
    l = []
    ct = 0
    for i in range(len(arr)):
        if arr[i] == False:
            l.append(ct)
            ct = 0
        else:
            ct += 1
    m = max(l)
    print(-1 if m == 0 else m)
