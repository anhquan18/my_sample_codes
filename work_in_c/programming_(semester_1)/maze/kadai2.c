#include <stdio.h>
#include "maze.h"
#include <stdlib.h>
/* （必要なら）関数の宣言． */

int main (void) {
  /* 変数の宣言． */
  /* 変数は自由に追加してよい． */
  int size, i;
  int turn[]={0,0}; 
  // turn[0] = left, turn[1] = right
  
  /* initialize関数は１度だけ呼ぶ． */
  /* 引数を自分の学生番号にすること． */
  initialize ("17C1054");

  for (int i = 0; i < 5000; i++) { 
    /* 迷路を作成する． */
    make_maze ();
    size = 1;
     while (check_goal ()!=1) {
  // printf("robot is still moving");
 
    if( check_wall_right() ) {
        if (check_wall_forward ()) { 
         rotate_left (); 
         turn[0]++;    }
        else { 
             step_forward (); 
              if ((turn[0] - turn[1]) % 4== 0) {
                size++; turn[0]=0; turn[1] = 0;
 }            if ((turn[1]-turn[0]==2) || (turn[0]-turn[1]==2)) {
                size--; 
           }
      }
}
    else {
    rotate_right (); turn[1]++;
    step_forward (); 
     if ((turn[0]-turn[1])%4==0) {
                size++; turn[0]=0; turn[1]=0;
}
    else if ((turn[1]-turn[0]==2) || (turn[0]-turn[1]==2)) {
                size--;
}

    
    
}
} 
   //if (size < 0) {size = -size;}
 /* if (size < 0) {  size = 0 - size;
}*/  
    /* 迷路を解き，サイズを測る． */

 size = abs(size);
 printf (" Maze %d\n\r",size);

    /* サイズを表示する */
}
  return 0;
}
