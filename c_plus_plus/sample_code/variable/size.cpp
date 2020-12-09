#include<iostream>
#include<cstddef>

using namespace std;


int incre()
{
    int a = 10;
    int b = 10;

    cout << a++ << endl;
    cout << a << endl;

    cout << ++b << endl;
    cout << b << endl;

    return 0;
}


int size()
{
    int x = 10;
    size_t size;

    size = sizeof ++x;
    cout << x << endl;
    cout << "size of x is " << size << endl;  // In byte

    return 0;
}


int size_of()
{
    int num = 50;
    char c = 'A';
    short s = 100;
    double d = 23.43;
    float f = 1.048f;
    long double ld = 1.234E-23;
    size_t sz;


    sz = sizeof num;
    cout << "int: " << sz << endl;

    sz = sizeof c;
    cout << "char: " << sz << endl;
    
    sz = sizeof d;
    cout << "double: " << sz << endl;

    sz = sizeof s;
    cout << "short: " << sz << endl;

    sz = sizeof f;
    cout << "float: " << sz << endl;

    sz = sizeof ld;
    cout << "long double: " << sz << endl;

    sz = sizeof (size_t);
    cout << "size_t: " << sz << endl;

    return 0;
}


int main()
{
    size_of();
    return 0;
}
