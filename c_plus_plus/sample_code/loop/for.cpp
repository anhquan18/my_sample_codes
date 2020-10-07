#include<iostream>
using namespace std;


void one_for()
{
    for(int i = 0; i < 10; i++)
    {
        cout << i << " times" << endl;
    }
}

void two_for()
{
    for(int x = 0; x <= 3; x++)
    {
        for(int y =0; y <= 3; y++)
        {
            cout << "x: " << x
                 << " y: "<< y 
                 << endl;
        }
    }
}

int main()
{
    two_for();
    return 0;
}
