#include<iostream>

using namespace std;

void n_ali()
{
    int num;
    int& alias_name = num; // must give ali_name the address when initial

    num = 10;

    cout << "num is "<< num << endl
         << "alias_name is "<< alias_name<< endl;

    alias_name = 100;

    cout << "num is "<< num << endl
         << "alias_name is "<< alias_name<< endl;
}

int main()
{
    n_ali();
    return 0;
}

