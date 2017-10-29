#include <stdio.h>
int main (void) {
char *str[] = {"international", "interesting"};
char *p1, *p2;
 int r =0;
 p1 = str[0];
 p2 = str[1];
  while (1) {
   if ((*p1 =='\0') && (*p2 =='\0')) { r=0; break;}
   if (*p1 < *p2) { r=-1; break;}
    else if (*p2 < *p1) { r=1; break;}
    else  { p1++; p2++;}
  if ((*p1 =='\0') && (*p2 =='\0')) { r=0; break;}
}
printf ("RESULT = %d\n", r);
return 0;
}
