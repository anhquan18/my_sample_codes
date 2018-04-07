#include<stdio.h>
#include<stdlib.h>


int main()
 {
   char c[4];
   double num[10]; 
   char cou;  
   
   printf("Input number");
   scanf("%c %s", &cou, c); num[0] = atof(cou  c);
   scanf("%c %s", &cou, c); num[1] = atof(cou  c);
   
   
   printf("%lf \n %lf \n", num[0], num[1]);
   /*
   printf(">>> ");
   c[0] = getchar();
   c[1] = getchar();
 
   //
   printf("%lf %lf", num[0], num[1]);
   
   printf("%c %c", c[0], c[1]);
   return 0; */
 }  
