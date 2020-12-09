#include "mbed.h"
#include "Motor.h"
#include <stdio.h>

int ADtoRad(float ad);

//change later
const float pen_r = 0.9;
const float 

Analogin pen (AD5);

int main()
{
    float KI,KD,KP;
    float theta;
    float ADtoRad = 2.0*3.14/1023;
    float x, theta;
    float wheel_s_left, wheel_s_right, accel, r_speed, angular_accel, angular_speed;
    float check_time = 0.01;

    while(1)
    {
        theta = ADtoRad(pen.read());
        angular_speed = theta / check_time;
        angular_accel = theta / check_time;
     
        r_speed = angular_speed * pen_r;


    }

}

int ADtoRad(float ad)
{
    double angle = ad * 2.0*3.14/1023;
    return angle;
}
