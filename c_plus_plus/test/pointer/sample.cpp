#include<iostream>

using namespace std;


void swap(int *a, int *b)  // You can also do this, since the value inside a function won't affect the value outside of it
{
    int z;
    
    z = *a;
    *a = *b;
    *b = z;
}


void p_in_p()
{
    int x;
    int *p1, **p2;

    p1 = &x;
    p2 = &p1;

    **p2 = 10;

    cout << "x is "<< x<< endl
         << "*p1 is"<< *p1<< endl
         << "**p2 is"<< **p2<< endl;
}


int main()
{
    int num, num2;
    int list[] = {1,2,3,4,5};
    int *p_num, *p_list = list;

    cout << &p_list[0]<< endl;

    p_num = &num;
    *p_num = 5; 
    num2 = 10;

    cout << "num = "<< num<< endl
         << "p_num = "<< p_num<< endl
         << "*p_num = "<< *p_num<< endl;

    p_num = &num2;
    cout << "num2 = "<< num2<< endl
         << "p_num = "<< p_num<< endl
         << "*p_num = "<< *p_num<< endl;

    swap(&num, &num2);

    cout << "num = "<< num<< endl
         << "num2 = "<< num2<< endl;

    p_in_p();

    return 0;
}
