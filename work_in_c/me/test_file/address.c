#include <stdio.h>


int main (void) 
{ 
    int a[]={1,3,4};
    int *p; 
 
    p=a;
    printf ("%p %p",p,&a[0]);
 
    return 0;
}
