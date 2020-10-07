#include<iostream>

using namespace std;

void check(int num)
{
    switch(num)
    {
        case 1:
            cout << "Yay it's 1" << endl;
            break;
        case 2:
            cout << "Yay it's 2" << endl;
            break;
        case 3:
            cout << "Yay it's 3" << endl;
            break;
        default:
            cout << "Yay it's a number" << endl;
    }
}


int main()
{
    int num;

    while(1)
    {
        cout << "Input number: ";
        cin >> num;

        check(num);

        if (num == 100) break;
    }
    return 0;
}
