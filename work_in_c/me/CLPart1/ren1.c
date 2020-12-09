#include<stdio.h>

int main(void){ 

int kubun,jinsu;

 printf ("input kubun and jinsu: ");
 scanf ("%d %d", &kubun,&jinsu);

 switch(kubun){
   case 1:
    printf ("料金は800、金額は%d\n",jinsu*800);
    break;
   case 2:
    printf ("料金は1000、金額は%d\n",jinsu*1000);
    break;
   case 3:
    printf ("料金は1500、金額は%d\n",jinsu*1500);
    break;
   default:
    printf ("Error, try some thing else\n");
}

return 0;
}

