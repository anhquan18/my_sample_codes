#include<stdio.h>
#include<string.h>

void main()
{
    char s, a;
 
    printf("input: ");
    scanf("%c", &s);
    scanf("%s", &a);
  
    printf("%c and %c\n", s, a);   
 
    if (strcmp(&a, "\n")==0)
        printf("It worked\n");
    else
        printf("Failed HAHAHAHA\nTry next time\n");
 
} 
