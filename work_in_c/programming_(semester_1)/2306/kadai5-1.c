#include <stdio.h>
int main(void) {
char str[] = "hello, world";
char *a;
 a=str;
 
 while (*a !='\0') {
putchar (*a);
 a++;
}
return 0;
}
