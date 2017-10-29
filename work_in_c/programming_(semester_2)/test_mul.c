#include<stdio.h>


int main()
 {
   unsigned long ans = 1;
   unsigned long i = 1;
   
   while(i <= 25) 
    { 
      ans *= i;
      i += 1;
    }
   
   i = 26;
   
   printf("%lu\n", ans * i);
   
   return 0;
 }
