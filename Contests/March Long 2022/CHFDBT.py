# cook your dish here
for t in range(int(input())):
    n = int(input())
    print(n // 2 if n % 2 == 0 else (n+1) // 2)
    '''sieve = [True for i in range(n+1)]
    sieve[0] = False
    for i in range(1, n+1):
        #print(sieve)
        print(i, sieve[i], end="\t")
        if sieve[i]:
            j = i * 2
            while(j <= n):
                print(j, end="\t")
                sieve[j] = False
                j *= 2
        print()
    print(sieve[1:n+1])
    print(sieve[1:n+1].count(True))'''