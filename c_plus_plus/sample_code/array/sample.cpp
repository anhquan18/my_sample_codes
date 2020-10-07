#include<iostream>

using namespace std;

void output_list()
{
    int list[5][3] = {{1,2,3},
                      {4,5,6},
                      {7,8,9},
                      {10,11,12},
                      {13,14,15}};

    for (int y=0; y < 5; y++)
        for (int x=0; x < 3; x++)
        {
            cout << list[y][x]<< endl;
        }
    cout << endl;

    for (int y=0; y < 5; y++)
        for (int x=0; x < 3; x++)
        {
            cout << &list[y][x]<< endl<< endl
                 << (list[y]+x)<< endl;
        }
    cout << endl;

    for (int y=0; y < 5; y++)
        for (int x=0; x < 3; x++)
        {
            cout << *(*(list + y) + x)<< endl;
        }
    cout << endl;


}

int main()
{
    output_list(); 
    return 0;
}
