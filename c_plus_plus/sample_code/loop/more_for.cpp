#include<iostream>
#include<iomanip>
#include<cmath>

using namespace std;

int main()
{
    const int genbun = 5;
    const double pi = 3.14;

    cout << "angle\tcos value:\timage" << endl;
    for (int i = 0; i < 70; ++i) cout << "-";

    for (int i = 90; i >= 0; i -=genbun) 
    {
        double rad = (pi * i) /180;
        double cos_value = cos(rad);

        cout << endl;
        cout << setw(2) << i << "\t" << fixed
             << setprecision(6) << cos_value << " ";

        for (int j = 0; j < int(cos_value * 40); ++j) 
            cout << "*";
    }
        cout << endl;
        return 0;
}
