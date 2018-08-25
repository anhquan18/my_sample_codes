#include<iostream>
using namespace std;


int checkSetf(int a, int b)
{
    cout << "Normal decimal number" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl << endl;

    cout << "Decimal display" << endl;
    cout.setf(ios::dec);
    cout << "a = " << a << endl;
    cout << "b = " << b << endl << endl;
    cout.unsetf(ios::dec);

    cout << "Hexadecimal dispay" << endl;
    cout.setf(ios::hex);
    cout << "a = " << a << endl;
    cout << "b = " << b << endl << endl;
    cout.unsetf(ios::hex);
    
    cout << "Octal display" << endl;
    cout.setf(ios::oct);
    cout << "a = " << a << endl;
    cout << "b = " << b << endl << endl;
}


int baseSetf(int a, int b)
{
    cout << "Decimal display" << endl;
    cout.setf(ios::dec, ios::basefield);
    cout << "a = " << a << endl;
    cout << "b = " << b << endl << endl;

    cout << "Hexadecimal dispay" << endl;
    cout.setf(ios::hex, ios::basefield);
    cout << "a = " << a << endl;
    cout << "b = " << b << endl << endl;
    
    cout << "Octal display" << endl;
    cout.setf(ios::oct, ios::basefield);
    cout << "a = " << a << endl;
    cout << "b = " << b << endl << endl;
}


int main()
{
    int a = 10, b = 100;
    
    checkSetf(a, b);
    baseSetf(a, b);

    return 0;
}

