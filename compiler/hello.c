#include <stdio.h>
int main(void){
float a;
float b;
printf("Enter the number a and b and the plus or minus operator\n");
if(0 == scanf("%f", &a)) {
a = 0;
scanf("%*s");
}
if(0 == scanf("%f", &b)) {
b = 0;
scanf("%*s");
}
printf("%.2f\n", (float)(a+b));
printf("%.2f\n", (float)(a-b));
return 0;
}
