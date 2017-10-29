#include<stdio.h>

int main(void)
 {
   int number;
   unsigned long long ansr = 1, i;
   int exit = 0;
   
   while(exit != 1) 
    {
      printf("\n>>> Input the number you want to caculate: ");
      scanf("%d",&number);
      
      if (number <= 0)
       {
         printf(">>> Please input one more time\n");
       } 
    
      else
       {
         for(i = 1; i <= number; i++) 
          {
            ansr *= i;
          }
      
         printf(" %llu\n\n", ansr);
         ansr = 1;   
       }   
     
      printf(">>> Choose 1 to exit, 0 to continue\n");
      printf(">>> Do you want to exit: "); 
      scanf("%d",&exit);  
     
    } 
   return 0;
 }

