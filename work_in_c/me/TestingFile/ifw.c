#include<stdio.h>


int main()
{
    int c, exit = 1;
   
    printf("input number: ");
    scanf("%d",&c);
   
    if (c == 1)
        while(exit != 0)
        {  
            printf("input exit: ");
            scanf("%d", &exit);
            printf("%d", exit);
        }
  
    return 0;
}
