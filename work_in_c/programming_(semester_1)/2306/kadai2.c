#include <stdio.h> 
 int main(void) {
char str[]= "hello, world";
 int i=0;
 while (1) {
 putchar(str[i]);
 i++;
 if ( str[i]== 0) {
 printf("\n");  break;}
}
return 0;
} 
