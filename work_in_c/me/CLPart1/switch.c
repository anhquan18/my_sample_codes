#include<stdio.h>

int main(void) {
 int kubun, tanka, suryo,ritsu;
 float money;

 printf ("input kubun: ");
 scanf("%d",&kubun);
 printf ("input tanka: ");
 scanf("%d",&tanka);
 printf ("input suryo: ");
 scanf("%d",&suryo); 

switch(kubun) {
  case 1:
     ritsu = 5;
     break;
  case 2:
     ritsu = 10;
     break;
  case 3:
     ritsu = 15;
     break;
  default:
     printf("Error: There is no such number.");
}
  money = tanka*suryo*(100-ritsu)/100;
  printf ("The total money is %f円\n", money);
  printf ("You got %d percents sale\n",ritsu);

return 0;
} 
