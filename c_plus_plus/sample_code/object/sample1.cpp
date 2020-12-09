#include<iostream>
#include<string>
using namespace std;

class MyClass 
{
    private:
        int num1;
    public:
        int id = 10;
        int num2;
        void set_num();
        void show_num();
        //void printname();
        void show_name();
        string name = "My class";

        //Default constructor
        MyClass()
        {
            cout << "Default constructor called" << endl;
            id -= 1;
            cout << id << endl;
        }
        
        //Parametrized Constructor
        MyClass(int num)
        {
            cout << "Parametrized constructor called" << endl;
            id = num;
            cout << id << endl;
        }

        //Copy constructor
        MyClass(const MyClass &old_class) {id = old_class.id; name = old_class.name;}
        //void printname()
        {
            cout << "Class name is: " << name << endl;
        }

    protected:
        int num3;
};

inline void MyClass::show_name()
{
    cout << name << endl;
}

void MyClass::set_num()
{
    cout << "Input num: ";
    cin >> num1; // access member without using self like python
}

void MyClass::show_num()
{
    cout << num1<< endl;
}

int main()
{
    cout << "main function" << endl;
    MyClass mc; //mc will call Default Constructor
    MyClass mc2(200); //mc2 will call Parametrized Constructor
    MyClass mc3 = mc; //Copy Constructor called
    //mc2 = mc1 Assignment constructor

    mc.num2 = 100; // You can set 
    mc.printname();
    mc3.printname();
}
