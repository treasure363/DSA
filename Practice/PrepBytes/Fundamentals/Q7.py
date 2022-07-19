N = int(input())

def brute(n):
    l = [0,1]
    for i in range(n):
        if i==0 or i==1:
            continue
        if i%2==0:
            l.append(l[int(i/2)])
        else:
            l.append(l[i-1] + 1)
    return l[-1]

    '''for i in range(len(l)):
        if i%2==0:
            print(i, '\t', l[i])
        else:
            print('\t', '\t', i, '\t', l[i])'''
        
def F(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        if n%2==0:
            return F(int(n/2))
        else:
            return F(n-1)+1
        
for i in range(N):
    print(brute(i), '\t', F(i))