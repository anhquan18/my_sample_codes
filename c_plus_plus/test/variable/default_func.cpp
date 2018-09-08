#include<iostream>

using namespace std;

float withTaxes(int money, float tax = 0.08)
{
    return money * tax;
}

int main()
{
    int money;
    
    cin >> money;
    cout << "Your taxes is "<< withTaxes(money)<< endl;

    return 0;
}
