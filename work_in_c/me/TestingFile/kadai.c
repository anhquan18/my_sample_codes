#include "stdio.h"



int main (void) 
{
    int i=0, z, backd, ford;
    int a[10];
   
 
    while (i < 10) 
    { 
        printf ("a[i] = %d\n", a[i]);
        scanf ("%d", & a[i]);
        i++; 
    }
    
    i = 0;
   
    while (i < 9) 
    { 
        for ( z = i+1; z < 10; z++) 
        { 
     	    if ( a[i] > a[z] ) 
            { 
                ford = a[i];   
                backd = a[z];
                
                a[i] = backd;  
                a[z] = ford;
            }
        }
      
        i++; 
    }
    
    i=0;
    
    while (i < 10) 
    { 
        if(i==9) {printf ("%d\n", a[i]);}
        else 
        { 
            printf ("%d ", a[i]); 
        }
        
        i++;
    }
 
    return 0;
}

