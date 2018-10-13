#include<iostream>
#include<iomanip>
using namespace std;


void intChar()
{
    char a='a';
    char b='b';
    char c='c';

    cout << int(a)<< endl
         << int(b)<< endl
         << int(c)<< endl;
}

void all_char()
{
    for (char ch = '!'; ch <= '~'; ch++)
    {
        cout << setw(3) << dec<< int(ch)
             << "(0x"<< hex<< int(ch)
             << ") -- "<< ch << " ";
        if ((ch - '!' + 1) % 4 == 0)
            cout << endl;
    }
    cout << endl;
}

void open_pointer()
{
    for(int i = 0; i < 3; i++)
        cout << *("ABC" + i)<< endl
             << "ABC"[i] << endl;
}

int main()
{
    open_pointer();
    return 0;
}
