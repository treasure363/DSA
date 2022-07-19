for t in range(int(input())):
    I = input()
    P = input()
    n, m = len(I), len(P)
    ind, ct = 0, 0
    updated = ""
    for i in range(n):
        print(I[i], ind, ct)
        while (ind < m) and (I[i] != P[ind]):
            ct += 1
            ind += 1
            print(ct)
            #print(P[ind], ind, ct, ind < m and I[i] != P[ind], I[i] != P[ind])
        print()
        if ind < m and I[i] == P[ind]:
            updated += I[i]
        print()
    print(updated, ind)
    if I == updated:
        print(m-ct)
    else:
        print("IMPOSSIBLE")
