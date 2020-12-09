#include <stdio.h>
#include "maze.h"

/* （必要なら）関数の宣言． */

int main (void) {
  /* 変数の宣言． */
  /* 変数は自由に追加してよい． */
  int turn[]={0,0};
  int size = 1;
 // long check[]={0,0};
  // turn[0] = left, turn[1] = right, check[0]=front, [1]=right
  
  /* initialize関数は１度だけ呼ぶ． */
  /* 引数を自分の学生番号にすること． */
  initialize ("17C1054");

  /* 迷路を作成する． */
  make_maze_with_size(5000);
 // while (i<=5001) {  
   while (check_goal ()!=1) {
    if(check_wall_right ())  {   
	if (check_wall_forward ()) { 
         rotate_left (); 
         turn[0]++; }
        else { 
             step_forward (); 
              if ((turn[0] - turn[1]) % 4== 0) {
                size++; turn[0]=0; turn[1] = 0;
   }          else if ((turn[1]-turn[0]==2) || (turn[0]-turn[1]==2)) {
                size--; 
}     
 
   
  } 
}
    else {//check[1]++;
    rotate_right (); turn[1]++;
    step_forward (); 
     if ((turn[0]-turn[1])%4==0) {
                size++; turn[0]=0; turn[1]=0;
}    else if ((turn[1]-turn[0]==2) || (turn[0]-turn[1]==2)) {
                size--; 
}    
    
}
} 
   printf("GOAL!!!!\n\r");
   printf("maze size is %d x %d\n", size,size);
  // printf("checkfront=%ld\ncheckright=%ld\n",check[0],check[1]);
   //printf("turnleft=%ld\nturnright=%ld\n",turn[0],turn[1]);
   //printf("forward with check=%ld\njust forward=%ld\n",forward[0],forward1]);  

 
  /* 迷路を解き，サイズを測る． */
  
 /* サイズを表示する. */

  return 0;
}
