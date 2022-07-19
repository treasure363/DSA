//Calculate factorial using the concept of function no argument,but return value
#include<stdio.h>

int fact(int n){
    int f = 1;
    while(n!=0){
        f *= n;
        --n;
    }
    return f;
}
    
void main(){
    int n;
    printf("Enter your number: ");
    scanf("%d", &n);
    fact(n);
}