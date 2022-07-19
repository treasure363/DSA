for t in range(int(input())):
    n= int(input())
    inp = input()
    s = [i for i in inp]
    #print(s)
    p = [i for i in inp]
    p.sort()
    for i in range(n//2):
        #print(s)
        #print(i, -(i+1), s[i], s[-(i+1)])
        if s[i] > s[-(i+1)]:
            t = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = t
            
    #print(s,p)
    if s==p:
        print("YES")
    else:
        print("NO")