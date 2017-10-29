#include <stdio.h>
 int main (void) {
 char str[23];
 printf("input characters into str: ");
 scanf("%s",str);
 str[22]='\0';
 printf ("%s\n",str);
return 0;
}
