#include<iostream>
#include<cstring>
#include<string>
using namespace std; 

void compare()
{
    char str1[20], str2[20];
    int cmp;

    cout << "Input str1: ";
    cin.getline(str1, 20);

    cout << "Input str2: ";
    cin.getline(str2, 20);

    cmp = strcmp(str1, str2);
    if (cmp < 0)
        cout << "first character doesn't match has lower value in str1 than str2"<< endl;
    else if(cmp == 0)
        cout << "str1 == str2\n";
    else
        cout << "first character doesn't match has greater value in str1 than str2"<< endl;
}


void length()
{
    char str[30];
    char name[] = "Quan";
    size_t len;

    cout << "Input string: ";
    cin.getline(str, 30);

    len = strlen(str);
    cout << "length of the string is "<< len<< endl;
}


void list_of_string()
{
    char str[8] = "abc";  // the value from str[3] to str[7] will be \0 null
    char *list;

    list = "Hello"; 
    /* With pointer you can input the whole string inside (adress value)
     * but with char a[10] you can't do that*/
    for(int i=0; i<7; i++)
        str[i] = 'a'+i;

    cout << list<< endl
         << str<< endl;
}


void input()
{
    char str[255];
    
    cin.getline(str, 255);
    /* the reason why we use getline and specific the buffer size is because 
     * with cin only some time the input will overload the buffer size and create something called 
     * overflow that is why we use getline*/
    cout << str<< endl;
}


void copy()
{
    char string[] = "abc";
    char *point;
    
    //can't use with pointer
    strcpy(string, "hi");

    cout << string<< endl
         << point<< endl;
}


void concatenate()
{
    char name[30], dono[] = " - dono";

    cout << "Input your name: ";
    cin.getline(name, 30);

    strcat(name, dono);
    cout << name<< endl;
}


void pointer_array()
{
    // have to declare it like this to make the array for pointer work, ussually used with const char
    
    const char *(arr[6]) = { "hellol",
                        "hi",
                        "no",
                        "yes",
                        "yay",};
    /* have to input string into pointer like this arr[2] = "string" if you want to change the whole value */
    cout << arr<< endl;
/*
    for (int i=0; i<6; i++)
        cout << arr[i]<< endl;
*/
    cout << "Check"<< endl;
    
    for (int j=0; j<6; j++)
        cout << &arr[j]<< endl;
}


void stg()
{
    // Different from list can expand from internal and as long as you have memory left you can make a longer string
    string str1;  // originally is std::string
    string str2;
    const string str3("Wow!");

    str1 = "Even cats can understand!";
    
    cout << "Input str2: ";
    cin >> str2;

    str1 += str3;
    str2 = "Hello new string, " + str2;

    cout << "str1: "<< str1<< endl;
    cout << "str2: "<< str2<< endl;
}



int main()
{
    pointer_array();
    return 0;
}
