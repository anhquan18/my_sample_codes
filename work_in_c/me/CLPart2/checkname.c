#include<stdio.h>

int main() {
  char *name[5];
  int i;
 for(i = 0;i < 5;i++) {
 printf("input your name: ");
 scanf("%s",name[i]);
 printf("%s",name[i]);
}

return 0;
}
