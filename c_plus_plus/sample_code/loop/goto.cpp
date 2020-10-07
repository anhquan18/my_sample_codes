#include<iostream>
#include<iomanip>

using namespace std;


void go()
{
    int i = 10;

    START:
    if (i > 0) 
    {
        cout << setw(2) << (11 - i) << " time" << endl;
        i--;
        goto START;
    }
}


int main()
{
    go();
    return 0;
}
