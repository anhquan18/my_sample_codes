#include<iostream>   // iomanip is include within so you can use it
#include<iomanip>    // inlcude to use setprecision
#include<bitset>     // use bitset

using namespace std;

const int a = 10, b = 200, c = 1024;
const double x = 12.123124, y = -3120000, z = 0.0004;


void bit_set()
{
    bitset<32>b_num(-2);
    cout << b_num << endl;
}

int nu_out()
{
    cout << "Normal output" << endl;
    cout << "a = " << a << ", b = " << b 
         << ", c = " << c << endl << endl;

    cout << " dec output" << endl;
    cout << dec << "a = " << a << ", b = " << b 
         << ", c = " << c << endl << endl;

    cout << " hex output" << endl;
    cout << hex << "a = " << a << ", b = " << b 
         << ", c = " << c << endl << endl;

    cout << " oct output" << endl;
    cout << oct << "a = " << a << ", b = " << b 
         << ", c = " << c << endl << endl;

    cout << " dec, hex, oct a" << endl;
    cout << dec << a << endl
         << hex << a << endl
         << oct << a << endl;
}

int float_fix()
{
    cout << fixed << "x = " << x << ", y = " << y 
         << ", z = " << z << endl << endl;

    cout << "scientific" << endl;
    cout << scientific << x << endl 
                       << y << endl
                       << z << endl;


    cout << "5 digits + normal" << endl;
    // won't turn normal if not use unsetf
    cout.unsetf(ios::scientific);
    cout << setprecision(5) << x << endl 
                       << y << endl
                       << z << endl;


    cout << "5 digits + scientific" << endl;
    cout << scientific << x << endl 
                       << y << endl
                       << z << endl;

    return 0;
}


int main()
{
    bit_set();
    return 0;
}
