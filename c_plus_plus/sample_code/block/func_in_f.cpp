#include<iostream>

using namespace std;

int kaijo(int i)
{
    /*
    if (i == 0)
        return 1;
    else
        return i * kaijo(i - 1);
    */
    return (i == 0) ? 1 : i * kaijo(i-1);
}


int main()
{
    int num;

    cin >> num;

    cout << num<< "! is "<< kaijo(num)<< endl;

    return 0;
}
