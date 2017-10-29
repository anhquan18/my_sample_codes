#include <stdio.h>

int main(void) {

int hour=0, minute=0,second;

 printf("input number of second: ");
 scanf("%d",&second);
 
 if(second < 60) {
      printf ("%d seconds = 0 hour 0 minute %d second(s)\n",second,second);
 
} else if((second >= 60) && (second < 3600)) {
      minute = second / 60;
      printf ("%d seconds = 0 hour %d minute(s) %d second(s)\n",second,minute,second % 60);
 
} else if (second >= 3600) {
      hour = second / 3600;
      minute = (second % 3600) / 60;
      printf("%d seconds = %d hour(s) %d minute(s) %d second(s)\n",second,hour,minute,(second % 3600) % 60);
 
} else {
      printf("ERROR: DO NOT INPUT ANY WEIRD THINGS\n");
}

return 0;
}
