#include<stdio.h>
#include<opencv2/opencv.hpp>
#include<opencv2/imgproc/imgproc.hpp>
#include<opencv2/highgui/highgui.hpp>

using namespace std;

// int blue(int a,int b, cv::Mat img0);
// int green(int z,int v, cv::Mat img1);
// int red(int c,int d, cv::Mat img2);


int main(void) {
 /*       //	Scalar green(0,250,100); 
        int thresh_hold = 3;
	cv::Mat src_img;	
	src_img = cv::imread("robocup_test.png",0);
	//エラー処理（画像が無い場合など）        
	if (src_img.empty()) return -1;
       // cv::Mat new_src_img = src_img + green;
        //cvtColor(new_src_img, new_src_img, cv::COLOR_RGB2GRAY);
   	double thresh = 100;
        double maxValue = 255; 
 
 // Binary Threshold
      cv:: threshold(src_img,src_img, thresh, maxValue, CV_THRESH_BINARY);

	//ウィンドウの名前、大きさ、縦横比
	cv::namedWindow("Image", CV_WINDOW_AUTOSIZE|CV_WINDOW_FREERATIO);	
 //	circle(src_img , center,25, blue, 1, 8, 0);			
	cv::imshow("Image", src_img);
	//キーボドを押すまでに待つ	
	cv::waitKey(0); 
} */



   
/*                  SPLIT 3 COLORS

    Mat Gi,Bi,Ri,fin_img;
    Gi = imread("robocup_test.png", CV_LOAD_IMAGE_COLOR);   // Read the file
    Bi = imread("robocup_test.png", CV_LOAD_IMAGE_COLOR);
    Ri = imread("robocup_test.png", CV_LOAD_IMAGE_COLOR);
  

  // namedWindow( "Display window", CV_WINDOW_AUTOSIZE );// Create a window for display.
                      // Show our image inside it.

    // Create Windows
      namedWindow("Red"  ,CV_WINDOW_AUTOSIZE);
      namedWindow("Green",CV_WINDOW_AUTOSIZE);
      namedWindow("Blue" ,CV_WINDOW_AUTOSIZE);

    // Create Matrices (make sure there is an image in input!)

    Mat green[3],red[3],blue[3];

    // The actual splitting.
    split(Gi, green);
   green[2]=Mat::zeros(Gi.rows, Gi.cols, CV_8UC1);//Set red channel to 0
   green[0]=Mat::zeros(Gi.rows, Gi.cols, CV_8UC1);//Set blue channel to 0

    split(Ri, red);
   red[1]=Mat::zeros(Gi.rows, Gi.cols, CV_8UC1);//Set green channel to 0
   red[0]=Mat::zeros(Gi.rows, Gi.cols, CV_8UC1);//Set blue channel to 0

    split(Bi,blue);
   blue[2]=Mat::zeros(Bi.rows, Bi.cols, CV_8UC1);//Set red channel to 0
   blue[1]=Mat::zeros(Bi.rows, Bi.cols, CV_8UC1);//Set green channel to 0
   
   
    //Merging Bi channels

    merge(blue,3,Bi);
    imshow("Blue", Bi);
    //Merging Gi channels
    merge(green,3,Gi);
    imshow("Green",Gi);
    //Merging Ri channels
    merge(red,3,Ri);
    imshow("Red",Ri);

    //imwrite("dest.jpg",image);

    waitKey(0);//Wait for a keystroke in the window
    return 0;
}
*/

//                 USING VEC3B
   cv::Mat Ni,old_img;

   Ni = cv::imread("robocup_test.png");
   old_img = cv::imread("robocup_test.png");
int x, y;
int blue ,red , green, row,col;
 
for(y = 1; y < Ni.rows - 1; y++) {
  for(x = 1; x < Ni.cols - 1; x++) {
     for(row = y - 1;row <= y + 1; row++) {
       for(col = x - 1; col <= x + 1; col++) {
          cv::Vec3b bgr = old_img.at<cv::Vec3b>(row,col);
          blue += bgr[0];
          green += bgr[1];
          red += bgr[2];   
       } 
     } 
  Ni.at<cv::Vec3b>(y,x) = cv::Vec3b(blue / 9,green / 9,red / 9);
  blue = 0; green = 0; red = 0;
  }  

}
 
 cv::namedWindow("Old_img" ,CV_WINDOW_AUTOSIZE);
 cv::namedWindow("New_img" ,CV_WINDOW_AUTOSIZE);

 cv::imshow("Old_img",old_img);
 cv::imshow("New_img",Ni);
 cv::waitKey(0);

 return 0;
}

//                               USING POINT 
/*
// 座標の設定
int x, y;
// 画像の読み込み
cv::Mat img = cv::imread("robocup_test.png");
cv::Mat3b new_img = img  
// 値の取得
// (0,0)が赤だった場合、BGRの順に"0,0,255"と出力される。
//cv::Vec3b bgr = new_img(cv::Point(x,y));
//printf("%d,%d,%d\n",bgr[0],bgr[1],bgr[2]);
// 値の設定
// (x,y)にBGR順に255,0,0(青)を設定する。
  for (y = 0; y < img.rows; y++) {
   for (x = 0; x < img.cols; x++) {
 
   new_img(cv::Point(x,y)) = cv::Vec3b(255,0,0);

 }
}
 cv::namedWindow("Look",CV_WINDOW_AUTOSIZE);
 cv::imshow("Look",img);
 cv::waitKey(0);
return 0;
}
*/

/*
// 座標の設定
int x, y;
// 画像の読み込み
cv::Mat img = cv::imread("robocup_test.png");
// 値の取得
// (0,0)が赤だった場合、BGRの順に"0,0,255"と出力される。
cv::Vec3b bgr = img.at<cv::Vec3b>(0,0);
printf("%d,%d,%d\n",bgr[0],bgr[1],bgr[2]);
// 値の設定
// (0,0)にBGR順に255,0,0(青)を設定する。
for (y = 0; y < img.rows; y++) {
  for (x = 0; x < img.cols; x++) {

 img.at<cv::Vec3b>(y,x) = cv::Vec3b(255,0,0);
 }
}
cv::imwrite("robocup.png",img);
return 0;
} */   
