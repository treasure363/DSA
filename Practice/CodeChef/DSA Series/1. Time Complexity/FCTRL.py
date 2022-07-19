import math

def zero(n):
    if n==0:
        return 0
    else:
        return math.floor(n/5)+zero(math.floor(n/5))

T = int(input())
for t in range(T):
    n = int(input())
    print(zero(n))