#include<iostream>


int main()
{
    int days = 365;
    int years = 4;
    int total_days = days * years;
    char e = 'A';

    std::cout << "total of days in" << years << " years is " << total_days << std::endl;
    std::cout << total_days << " - " << days << " = " << total_days - days << std::endl;
    std::cout << "inside A is " << (int)e << std::endl;

    for (int i = 0; i < 150; i += 30)
    {
        std::cout.width(5);          // Fix the length of the output
        std::cout.fill('*');         // Fill the white space(empty) with char
        std::cout << i << std::endl; // Only active one
        std::cout << i+100 << std::endl;
    }

    return 0;
}
