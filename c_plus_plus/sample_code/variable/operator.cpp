#include<iostream>
#include<bitset>

using namespace std;

#define CAT 1  //bit 0001
#define DOG 2  
#define RAT 4
#define RABBIT 8


void normalOp()
{
    int a = 3;
    double b = 10.34;

    cout << "a + b = " << a + b << endl;
}


void bitOp()
{
    int a = CAT | DOG;
    int b = RAT;
    int c = CAT | DOG |RAT | RABBIT;
    int d = DOG | RAT;

    cout << a << endl 
         << b << endl
         << c << endl 
         << d << endl;

    cout << "A's pet cat " << ((a & CAT) != 0)
         << ", dog = " << ((a & DOG) != 0)
         << ", rat = " << ((a & RAT) != 0)
         << ", rat = " << ((a & RABBIT) != 0) << endl;

    cout << "B's pet cat " << ((b & CAT) != 0)
         << ", dog = " << ((b & DOG) != 0)
         << ", rat = " << ((b & RAT) != 0)
         << ", rat = " << ((b & RABBIT) != 0) << endl;

    cout << "C's pet cat " << ((c & CAT) != 0)
         << ", dog = " << ((c & DOG) != 0)
         << ", rat = " << ((c & RAT) != 0)
         << ", rat = " << ((c & RABBIT) != 0) << endl;

    cout << "D's pet cat " << ((d & CAT) != 0)
         << ", dog = " << ((d & DOG) != 0)
         << ", rat = " << ((d & RAT) != 0)
         << ", rat = " << ((d & RABBIT) != 0) << endl;
}


void shiftOperator()  // shift the bit digit to the left or right
{
   short a = 12, b = 100, c = -255;

   cout << a << " shift to left by 1 " << (a << 1) << endl
             << " shift to left by 2 " << (a << 2) << endl
             << " shift to left by 3 " << (a << 3) << endl
             << " shift to left by 4 " << (a << 4) << endl;
   cout << endl;
   cout << b << " shift to left by 1 " << (b << 1) << endl
             << " shift to left by 2 " << (b << 2) << endl
             << " shift to left by 3 " << (b << 3) << endl
             << " shift to left by 4 " << (b << 4) << endl;
   cout << endl;
   cout << c << " shift to left by 1 " << (c << 1) << endl
             << " shift to left by 2 " << (c << 2) << endl
             << " shift to right by 1 " << (c >> 1) << endl;

   bitset<16>m_num(32767);
   bitset<16>m_num2(-32767);
   bitset<16>m_num3(-2);
   bitset<16>m_num4(c);

   cout << m_num << endl;
   cout << m_num2 << endl;
   cout << m_num3 << endl;
   cout << m_num4 << endl;
}
 

void condOP()
{
    (100 > 1434) ? (cout << "It is True") : // when it is true
                   (cout << "It is False");
    /* ternary operator
     * binary operator
     * unary operator
     */
}

int main()
{
    condOP();
    return 0;
}
