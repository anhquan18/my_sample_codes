#include<stdio.h>

int main (void){

 char name[20],nick[]={'d','a'};
 int year;
   
   printf ("input your name: ");
   scanf("%s",name);
   printf ("input year: ");
   scanf ("%d",&year);
   printf("input nickname: ");
   scanf("%c %c",&nick[0],&nick[1]);

if ((nick[0] == 'c') && (nick[1] == 'u')) {
   printf ("%s your age is %d\n",name,year - 2000);
}
else {
   printf ("I dont know anyone name %s\n",name);
}


return 0;
}


