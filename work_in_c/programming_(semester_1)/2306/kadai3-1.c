#include <stdio.h> 
 int main (void) {
 int x=1,y=3,z=5;
 int *p;
 p = x;
 printf ("%p %p %p\n",p,&y,&z);
return 0;
}

