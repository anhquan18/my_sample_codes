#include<iostream>
#include<typeinfo>

using namespace std;


int cast()
{
    int a, b;

    a = 10; b = 4;

    cout << "a / b = " << a / b << endl;
    cout << "a / b = " << (double)a / b << endl;
    cout << "a / b = " << double(a) / b << endl;
    cout << "char is " << char(65) << endl;

    // You can't use this to change type and put it into other variable
}


int high_cast()
{
    float f = 12.345;
    int i;

    const int a = 20;
    const int *p = &a;
    int *pp = const_cast<int *>(p);  // remove the const of the variable

    long l = 1234;
    int *pi = reinterpret_cast<int *>(&l);  // usually used to turn normal type into pointer and reverse

    cout << typeid(l).name() << endl;
    

    i = static_cast<int>(f);
    
    cout << i << endl;
    cout << f << endl;

    //*p = 1; can't chagne the value
    *pp = 1;

    cout << *pp << endl;
    cout << p << endl;

    return 0;
}


int main()
{
    high_cast();
    return 0;
}
