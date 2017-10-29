#include <stdio.h>
int main (void) {
char c = 'A';
 while (c <= 'z') {
 putchar(c);
 if (c=='Z') { c='`';
  printf ("\n");}
 c++;
}
return 0;
}
