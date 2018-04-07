#include <stdio.h>


int lcd(int b[],int c);


int main (void) 
{
    int s;
    int a[] = {54, 6,48,60};
 
    s = lcd (a, 4);
 
    printf ("%d",s);
 
    return 0;
}



int lcd(int b[],int c)
{
    int i=1, j;
    int count, bye;
    int back = 0;
 
    while (back != 1) 
    { 
        count = 0;
        for (j=0 ;j <= c-1;j++) 
        {
            if (i % b[j] == 0)
            {
                count++;
                if (count == c) 
                {
                    bye = i; back =1; 
                }
            }
        }     
        
        i++;
    } 
    
    return bye;
}   


