#include <stdio.h>
 #include <math.h>
  double dist (double,double,double,double);
  double d;
 int main (void){
  double x1=2.0, x2=5.0, y1=4.0, y2=3.0;
  d = dist (x1,x2,y1,y2);
  printf ("d=%lf\n",d);
return 0;
}
  double dist (double x1, double x2, double y1, double y2) { 
 #include <math.h>
   double d, a= (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
  d = sqrt (a);
 return d;
}
