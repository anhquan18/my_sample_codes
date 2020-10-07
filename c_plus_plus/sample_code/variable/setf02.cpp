#include<iostream>
using namespace std;


int main()
{
    double d1 = 3.13, d2 = 1000.0, d3 = -12.32425;

    cout << "Display number in the right" << endl;
    cout.setf(ios::right, ios::adjustfield);
    cout << "d1 = ";
    cout.width(10);
    cout << d1 << endl;

    cout << "d2 = ";
    cout.width(10);
    cout << d2 << endl;

    cout << "d3 = ";
    cout.width(10);
    cout << d3 << endl;

    cout << "Fixed .. number" << endl;
    cout.setf(ios::fixed, ios::floatfield);
    cout << "d1 = " << d1 << endl;
    cout << "d2 = " << d2 << endl;
    cout << "d3 = " << d3 << endl;

    cout << "科学技術計算表示" << endl;
    cout.setf(ios::scientific, ios::floatfield);
    cout << "d1 = " << d1 << endl;
    cout << "d2 = " << d2 << endl;
    cout << "d3 = " << d3 << endl;

    return 0;
}
