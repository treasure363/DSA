#include <stdio.h>
#include <math.h>

long long fact(long n){
    if(n==0)    return 1;
    if(n==1)    return 1;
    return n*fact(n-1);
}

long long combination(long n, long r){
    return fact(n)/(fact(r)*fact(n-r));
}

int main(void){
    int a, b, n;
    scanf("%d%d%d", &a, &b, &n);
    long long sum = 0;
    for(int i=0; i<=n; ++i)
        sum += combination(n, i) * pow(a, n-i) * pow(b, i);
    printf("%lld", sum);
    return 0;
}