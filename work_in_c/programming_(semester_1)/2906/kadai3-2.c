#include <stdio.h>
int sum(int *x,int y);
int main (void ) {
 int b,a[]={1,5,9,2,10,15};
 b =sum(a,6);
 printf ("%d\n",b);
return 0;
}

int sum(int *x,int y){
int i=0,z=0;
 while(i<y){
 z+=*x;
 x++;
 i++;
}
return z;
}
