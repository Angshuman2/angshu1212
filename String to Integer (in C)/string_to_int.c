#include <stdio.h>
int num(int n){
    int n1;
    if(n!=1){
        n1=1;
        for(;n!=1;n--){
            n1*=10;
        }
    }
    else{
        n1=1;
    }
    return n1;
}
int integer(char *arr){
    int a=0,a1=0;
    for(;arr[a]!='\0';a++){
        a1++;
    }
    int a3=a1;
    int sum=0,a2=0;
    for(;a2!=a1;a2++,a3--){
        if((int)arr[a2]>=48 && (int)arr[a2]<=57){
            sum=sum+(((int)arr[a2]-48)*num(a3));
        }
        else{
            sum=0;
            printf("space,special character and alphabet can not change into integer....\n");
            break;
        }
    }
    return sum;
}

int main(){
    char number[]="010212";
    printf("%d\n",integer(number));
}