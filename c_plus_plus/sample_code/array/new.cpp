#include<iostream>
#include<string>
using namespace std;

void sample1()
{
    /* new date_type[number] will storage the new data needed and can be deleted later when don't need any more with delete [] pointer*/
    int *p;
    cout << "Enter the amount of needed number: ";
    int number;
    cin >> number;

    p = new int[number];
    
    for(int i=0; i < number; i++)
    {
        cout << "value for need["<< i+1<< "]: ";
        cin >> p[i];
    }

    for (int i=0; i < number; i++)
        cout << p[i]<< endl;
    
    delete [] p;  // delete the uneccessary memory
}

void sample2()
{
    string* name = new string[4]; // Storage 4 string
    
    for(int i=0; i< 4; i++)
    {
        cout << "Input name: ";
        // get string from cin for input_string
        string input_string; // String is real useful cause you don't need to define the size of the buffer
        getline(cin, input_string); /* std::getline the argument for it is istream& and string& 
                                       if you want to know more google it*/

        // storage name as member of the list
        name[i] = input_string;
    }
    
    for (int i = 0; i < 4; ++i)
        cout << name[i]<< endl;

    delete[] name; // free the memory
}

int main()
{
    sample2();
    return 0;
}
