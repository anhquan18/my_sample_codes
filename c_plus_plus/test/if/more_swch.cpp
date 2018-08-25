#include<iostream>
using namespace std;


int main()
{
    int c;
    char buf[16];

    while(c != 'x')
    {
        cout << "Input somethings fun: " << endl;
        cout << "a , b , c, x" << endl;

        while(1) 
        {
            cin.getline(buf, 16);
            cout << "You input: " << buf << endl;
            c = buf[0];
            if (c != '\n')
                break;
        }

        switch(c)
        {
            case 'a':
                cout << endl;
                cout << "a pressed" << endl;
                break;

            case 'b':
                cout << endl;
                cout << "b pressed" << endl;
                break;

            case 'c':
                cout << endl;
                cout << "c pressed" << endl;
                break;
        }

    }
    return 0;
}
