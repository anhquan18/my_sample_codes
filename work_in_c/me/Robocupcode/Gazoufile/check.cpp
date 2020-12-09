#include<stdio.h>
#include<opencv2/opencv.hpp>
#include<opencv2/imgproc/imgproc.hpp>
#include<opencv2/highgui/highgui.hpp>

using namespace cv;

// 座標の設定
int x, y;
// 画像の読み込み
Mat img = cv::imread("robocup_test.png");
// 値の取得
// (0,0)が赤だった場合、BGRの順に"0,0,255"と出力される。
Vec3b bgr = img.at<Vec3b>(x,y);
printf("%d,%d,%d\n",bgr[0],bgr[1],bgr[2]);
// 値の設定
// (x,y)にBGR順に255,0,0(青)を設定する。
for (y = 0; y < img.rows; y++) {
  for (x = 0; x < img.cols; x++) {

  srcImg.at<Vec3b>(x,y) = Vec3b(255,0,0);
 }
}
 namedWindow("Look",CV_WINDOW_AUTOSIZE)
 imshow("Look",img);
 waitKey(0);
return 0;
}
