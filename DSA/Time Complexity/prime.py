from time import time

#function 1
def method1(n):
    var = 0
    for i in range(2, n-1, 1):
        if n%i==0:
            var = 1

    if var==1:        
        return False
    else:
        return True

#function 2
def method2(n):
    i = 2
    var = 0
    while(i*i<=n):# --> i <= sqrt(n)
        if n%i==0:
            var = 1
        i += 1
    if var==1:
        return False
    else:
        return True

n = int(input("Enter your number: "))
t1 = time()
print(method1(n), time()-t1)

t1 = time()
print(method2(n), time()-t1)