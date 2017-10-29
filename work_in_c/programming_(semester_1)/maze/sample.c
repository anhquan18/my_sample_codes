/* 手動でロボットを動かす例 */
#include <stdio.h>
#include "maze.h"

int main (void) {
  /* 変数宣言 */
  char command = '\0';   /* 何をするか */
  char direction = '\0'; /* 方向 */
  char r = '\0';         /* 改行を受け取るためダミー */
  
  /* initialize関数は最初に1度だけ呼ぶこと. */
  /* 引数は自分の学生番号にすること. */
  initialize ("17C9999");

  /* 迷路が作成される */
  make_maze_with_size (3);
  
  while (check_goal () != 1) {
    printf ("command (c, r, s): ");
    scanf ("%c%c", &command, &r);
    if (command == 'c') {
      printf ("direction (f, r, l, b): ");
      scanf ("%c%c", &direction, &r);
      if (direction == 'f') {
	if (check_wall_forward ()) {
	  printf ("TRUE\n");
	} else {
	  printf ("FALSE\n");
	}
      } else if (direction == 'r') {
	if (check_wall_right ()) {
	  printf ("TRUE\n");
	} else {
	  printf ("FALSE\n");
	}
      } else if (direction == 'l') {
	if (check_wall_left ()) {
	  printf ("TRUE\n");
	} else {
	  printf ("FALSE\n");
	}
      } else if (direction == 'b') {
	if (check_wall_backward ()) {
	  printf ("TRUE\n");
	} else {
	  printf ("FALSE\n");
	}
      } else {
	printf ("unknown direction\n");
      }
    } else if (command == 'r') {
      printf ("direction (r, l): ");
      scanf ("%c%c", &direction, &r);
      if (direction == 'r') {
	rotate_right ();
      } else if (direction == 'l') {
	rotate_left ();
      } else {
	printf ("unknown direction\n");
      }
    } else if (command == 's') {
      printf ("direction (f, b): ");
      scanf ("%c%c", &direction, &r);
      if (direction == 'f') {
	if (step_forward()) {
	  printf ("SUCCESS\n");
	} else {
	  printf ("FAILURE\n");
	}
      } else if (direction == 'b') {
	if (step_backward()) {
	  printf ("SUCESS\n");
	} else {
	  printf ("FAILURE\n");
	}
      } else {
	printf ("unknown direction\n");
      }
    } else {
      printf ("unknown command\n");
    }
  }
  printf ("GOAL!\n");
  
  return 0;
}
