m = 1000000007
def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base %= modulus
    while exponent>0:
        if exponent % 2 == 1:
            result = (result*base) % modulus
        exponent >>= 1
        base = (base*base) % modulus
    return result

for t in range(int(input())):
    a, b, c = map(int, input().strip().split())
    print(modular_pow(modular_pow(a, b, m), c, m))