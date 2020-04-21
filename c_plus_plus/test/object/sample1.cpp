#include<iostream>
using namespace std;

class MyClass 
{
    private:
        int num1;
    public:
        int num2;
        int set_num();
        int show_num();
};

void MyClass::set_num()
{
    cout << "Input num: ";
    cin >> num1;
}

void MyClass::show_num()
{
    cout << num1<< endl;
}

int main()
{
    MyClass mc;

    mc.num2 = 100; // You can set 
}
