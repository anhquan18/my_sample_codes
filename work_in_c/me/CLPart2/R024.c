#include<stdio.h>

int main() {
 int kensu = 1, goukei = 0, tensu, max = 0, min = 10000;
 printf("Input some tensu you like: ");
 scanf("%d",&tensu);
 goukei += tensu;
 
 while (tensu != 999) {
   printf("Input some tensu won't you: ");
   scanf("%d",&tensu);
   goukei += tensu;
   if (tensu > max) { max = tensu; }
   if (tensu < min) { min = tensu; }
   kensu++;
}
 
 printf("the average tensu is %d, goukei is %d\n",goukei / kensu, goukei);
 printf("Max tensu is %d, min tensu is %d\n", max, min);

return 0;
}
