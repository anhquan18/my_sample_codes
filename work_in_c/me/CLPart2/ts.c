#include <stdio.h>
#include<string.h>

int main(){
  int maxh=0,height,i=0;
  char name[20],maxname[20];
  
  while (i<5) {
    printf ("input name: ");  
    scanf("%s", name); 
    printf ("input height: ");   
    scanf("%d",&height);
      i++;
      if (height > maxh) {
         maxh = height;
         strcpy(maxname,name);
  }
}
  printf("The tallest person is %s and with %d height\n",maxname,maxh);

return 0;
}
    
    
   
