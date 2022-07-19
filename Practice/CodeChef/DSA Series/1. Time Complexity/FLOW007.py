T = int(input())
for t in range(T):
    n = int(input())
    m = 0
    while(n!=0):
        m = m*10 + n%10
        n //= 10
    print(m)