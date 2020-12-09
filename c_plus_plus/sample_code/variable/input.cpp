#include<iostream>

using namespace std;


int twoNum()
{
    int x, y;


    cout << ">> x: ";
    cin >> x;

    cout << ">> y: ";
    cin >> y;

    cout << "the result of x: "<< x << " and y: " << y << endl;
    cout << "the sum: " << x + y << endl;

    return 0;
}


int many()
{
    int a, b, c, d;

    cout << "a, b, c, d:  ";
    cin >> a >> b >> c >> d;

    cout << "sum of a,b,c,d is " << a+b+c+d << endl;
    return 0;
}


int main()
{
    //twoNum();
    many();
    
    return 0;
}
