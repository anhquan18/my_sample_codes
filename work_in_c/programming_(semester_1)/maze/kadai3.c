#include <stdlib.h>
#include <stdio.h>
#include "maze.h"

/* （必要なら）関数の宣言． */

int main (void) {
  /* 変数の宣言． */
  /* 変数は自由に追加してよい． */
  int i,size,a[] = {0,0,0,0,0,0,0,0,0,0,0};
  int turn[]={0,0}; 
  //a[0] 0-100 , a[1] 100 - 200,...,a[9] 900 - 1000
  /* initialize関数は１度だけ呼ぶ． */
  /* 引数を自分の学生番号にすること． */
  initialize ("17C1054");

  for (int i = 0; i < 5000; i++) {
    /* 迷路を作成する． */
    make_maze ();
    size = 1;
    /* 迷路を解き，サイズを測る． */

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

 size = abs(size);
 if ((0<size) &&(size<=100))      { a[0]++;}
 else if ((100<size) &&(size<=200)) { a[1]++;}
 else if ((200<size) &&(size<=300)) { a[2]++;}
 else if ((300<size) &&(size<=400)) { a[3]++;}
 else if ((400<size) &&(size<=500)) { a[4]++;}
 else if ((500<size) &&(size<=600)) { a[5]++;}
 else if ((600<size) &&(size<=700)) { a[6]++;}
 else if ((700<size) &&(size<=800)) { a[7]++;}
 else if ((800<size) &&(size<=900)) { a[8]++;}
 else if ((900<size) &&(size<=1000)) {a[9]++;}
 else if ((100<size) &&(size<=200)) { a[10]++;}
 //else if ((100<size) &&(size<=200)) { a[1]++;}

//printf ("GOAL!!! Maze size is %d x %d\n\r",size,size);
 

    /* ヒストグラムを更新する． */
 }
 i = 1;

while(i<=11){ 
if (i!=11 ){ printf("There are %d maze's size %d\n",a[i-1],i*100);
}else {  printf("There are %d maze's size over 1000\n",a[10]);
}
 
i++;
}

  /* ヒストグラムを表示する． */
  
  return 0;
}
