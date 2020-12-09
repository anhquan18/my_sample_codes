#include <stdio.h>

int main (void) 
 {
   int x, y;
   float z;
   
   printf ("input x: ");
   scanf("%d",&x);
 
   printf ("input y: ");
   scanf("%d",&y);

   z = x % y;

   printf ("amari is %f\n", z);

   return 0;
 }
