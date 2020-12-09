#include<stdio.h>

int main(){

 int second,h,m,s;
 
 printf("input number of second: ");
 scanf("%d",&second);

 m = second/60;
 h = m / 60;
 s = second % 60;
 m = m % 60;
 
 printf ("%d　秒 = %d　時間 %d　分 %d 秒\n",second,h,m,s);

return 0;
}
