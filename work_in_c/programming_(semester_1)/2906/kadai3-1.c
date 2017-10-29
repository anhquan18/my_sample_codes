#include <stdio.h>
 void strupper (char*a) ;
int main (void) {
char str[] = "Hello, World!";
 strupper(str);
 printf ("%s\n",str);
return 0;
}
 void strupper (char*a){
while(*a!='\0') {
 if (*a >= 'a') {*a -=32;
 
}
  a++;
}
 
return ;
}
