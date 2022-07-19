//Calculate factorial using the concept of function argument,but no return value
#include<stdio.h>

void fact(int n){
    int f = 1;
    while(n!=0){
        f *= n;
        --n;
    }
    printf("Factorial: %d", f);
}
    
void main(){
    int n;
    printf("Enter your number: ");
    scanf("%d", &n);
    fact(n);
}