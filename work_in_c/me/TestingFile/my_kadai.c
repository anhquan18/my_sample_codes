#include<stdio.h>
#include<string.h>

void main()
{
    char str[20];
    int i = 0;  
  
    while(1)
    {
        scanf("%s", str);
        
        printf("%s\n", str);
        printf("%d\n", i);
      
        i++;
     
        if(strcmp(str, "\n") == 0)
            break;
    }
   
    printf("It ends here\n");
   
}
