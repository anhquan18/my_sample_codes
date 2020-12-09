/* 初期化を行う. strには学籍番号の文字列の先頭アドレスを渡すこと. */
/* プログラムの最初に１度だけ呼ぶこと. */
extern void initialize (const char *str);

/* 迷路を作成する */
extern void make_maze (void);

/* 迷路を作成する（サイズを指定する） */
extern void make_maze_with_size (int n);

/* ロボットの状態を初期化する（迷路のスタート地点に戻し，上を向ける） */
extern void reset_robot (void);

/* ロボットの前方に壁があるかを調べる */
extern int check_wall_forward (void);

/* ロボットの右側に壁があるかを調べる */
extern int check_wall_right (void);

/* ロボットの後方に壁があるかを調べる */
extern int check_wall_backward (void);

/* ロボットの左側に壁があるかを調べる */
extern int check_wall_left (void);

/* 前方に1歩進む. 
   成功した場合は 1 が戻る.
   前方に壁があり失敗した場合は 0 が戻る. */
extern int step_forward (void);

/* 後方に1歩進む. 
   成功した場合は 1 が戻る.
   後方に壁があり失敗した場合は 0 が戻る. */
extern int step_backward (void);

/* 右に90度回転する */
extern void rotate_right (void);

/* 左に90度回転する */
extern void rotate_left (void);

/* ゴールにいるかどうかを確認する．
   ゴールにいる場合は1，そうでない場合は0が戻る．
*/
extern int check_goal (void);
