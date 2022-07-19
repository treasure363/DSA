//wap to accept three number check if the biggest no. is prime or not using argument but no return value
#include<stdio.h>

void prime(int n);

void main(){
    int a,b,c;
    printf("Enter your numbers: ");
    scanf("%d%d%d", &a, &b, &c);
    if(a>b){
        if(a>c)
        prime(a);
        else
        prime(c);
    }
    else{
        if(b>c)
        prime(b);
        else
        prime(c);
    }
}

void prime(int n){
    printf("%d is the biggest number\n", n);
    int f=0;
    for(int i=2; i<n; ++i)
    if(n%i==0){
        f=1;
        break;
    }
    if(f==0)
    printf("%d is a Prime Number", n);
    else
    printf("%d is a not a Prime Number", n);
}