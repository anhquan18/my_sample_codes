#include<iostream>

using namespace std;

int main()
{
    int num = 10;

    /* condition mark help you shorten the code
     * condition ? code_if_true : code_if_false
     * much shorter then the if else
     * can be used like this as well
     * return (condition) ? result_if_true : result_if_false
     */

    (num > 0) ? cout << num<< endl: cout << "smaller than 0"<< endl;

    return 0;
}
