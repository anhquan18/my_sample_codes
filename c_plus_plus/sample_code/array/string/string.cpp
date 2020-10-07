#include<iostream>
#include<string>
using namespace std;

void output(string name="", string word="")
{
    cout << name << word;
}

int main()
{
    string str1, str2;
    string str3("WOW!!!!");

    str1 = "Even I can do";
    
    cout << "Input str2: ";
    cin >> str2;

    str1 += str3;
    str2 = "You have inputed: " + str2;

    cout <<"str1: "<< str1 << endl;
    cout <<"str2: "<< str2 << endl;

    cout << "str1 size: "<< str1.length()<< endl;
    cout << "str1[1]: "<< str1[1]<< endl;

    output("Quan", "hello");

    // if found can string::npos will be returned
    size_t index = str1.find("can");

    if(index != string::npos)
        // Output 3 char from index
        cout << "first character "<< str1.substr(index, 3) << endl;

    if (str3 == "WOW!!!!")
        cout << "str3 met the condition"<< endl;
    if(str3 != "CAt")
        cout << "str3 didn't meet the condition" << endl;
    return 0;
}
