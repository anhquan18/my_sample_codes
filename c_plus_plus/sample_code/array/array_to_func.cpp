#include<iostream>
using namespace std;

void show_array(int x[]) // you can put int *x or int * insde the argument
{
    for(int i=0; i<3; i++)
        cout << x[i]<< endl;
}

void show_charaters(const char **name) // error will come out if you use char *name
{
    for(int i=0; i<5; i++)
        cout << name[i]<< endl;
}

void show_2d_array(int list[][2]) // you can give the argument int m[][2] or int ** or int(*m)[2] as well
{
    for (int x=0; x < 4; x++)
        for(int y=0; y < 2; y++)
            cout << list[x][y]<< endl;
}

int main()
{
    int list_1d[3] = {10, 20, 30};
    const char *name[] = {"Tom",
                          "Thomas",
                          "Quan",
                          "Matsu",
                          "Og"};
    int list_2d[][2] = {{1, 2},
                  {3, 4},
                  {5, 6},
                  {7, 8}};

    show_2d_array(list_2d);
    show_charaters(name);
    show_array(list_1d);
    return 0;
}
