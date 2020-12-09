#include<stdio.h>

int main(){
   int gokei=0,max=0,min=99999,i,x;

 for(i=0;i<10;i++) {

  printf("input some x wont you: ");
  scanf("%d",&x);
  if (x<=min) { min = x;}
  if (x>=max) { max = x;}
  gokei += x;
}

printf ("gokei: %d\nmax: %d\nmin: %d\n",gokei,max,min);

return 0;
}
   
  
