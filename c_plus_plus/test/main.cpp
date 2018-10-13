#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(int argc, char *argv[])
{
    cout << argc << endl;
    cout << argv << endl;

    for(int i=0; i < argc; i++)
        cout << *argv[i]<< endl;

    vector<string>args(&argv[0], &argv[argc]);

    for (auto s: args)      // access to all variables inside array
        cout << s << endl;  

    return 0;
}
