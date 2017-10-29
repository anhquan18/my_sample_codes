#include <stdio.h>
int main (void) {
char str[11];
int i=0;
char c;
while (c != '\n') {

c = getchar();
str[i] = c;
i++;
}

printf ("%s\n",str);
//putchar(str);
return 0;
}
