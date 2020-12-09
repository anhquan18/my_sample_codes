#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{   
    char str[20], n; 
    double num;   
 
    printf("input digit: ");
    scanf("%c", &n);
    strcpy(str, &n);  
  
    num = atof(&str[0]);
    printf("%lf\n", num);   
 
    if (atof(&str[0]))
    { 
        strcat(str, "000");
    }
    
    printf("%c\n",str[1]);
    printf("%s\n", str);
    num = atof(str);
    printf("%lf\n", num);
  
    return 0;
}
