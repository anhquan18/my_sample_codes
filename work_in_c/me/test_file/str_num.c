#include<stdio.h>

void main()
{
    char str = '0';
 	
    while(str != '\n')
    {    
        printf(">>> ");
        scanf("%c", &str);
        printf("str.num: %d, str.char: %c\n", str, str);
 	}
 	
}
