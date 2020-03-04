#include<iostream>
using namespace std;


int main()
{
    //short x;        // 16 bit now
    //int y;          // 32 bit now -2**31 -> 2**31 - 1
    //long z;         // 32 bit now equal to int so not usually used now

    //float f_a;        // 32 bit
    //double b;       // 64 bit
    //long double d;  // 64 bit

    //char c;         // 8 bit

    static int i = 0;
    extern int global_i;   // for global variable

    /* Under score:
       1. Having global scope, start with _
       2. Start with _ and next is Uppercase
       3. Having __ within */

    const double pi = 3.141592;
    const int buffer_size = 255;

    auto pi_num = 3.14; // 型推論
    auto e = 1;

    int name1 = 10;
    int& ref = name1; // reference 参照 using a different name for variable 
    int &ref2 = name1, &ref3 = name1; // ref2,3 are references
    int &ref4 = name1, name2 = name1; // ref4 is reference, name2 is int
    ref = 15; // name1 value also changes after ref changes

    int a_test = 10;
    int *pA = &a_test; // initialize pointer using a_test's address
    /* int *pA = addressof(a_test); */
    *pA = 20; // access and edit value of a_test using pointer
    int **ppA = &pA; // pA's pointer, pointer's pointer ppA --> pA --> a_test
    int *pA2; // pA --> a_test <-- pA2

    pA2 = pA;

    cout << **ppA << endl;
    cout << *pA2 << endl;

    // ####################################################################################
    // 型の別名を宣言 typedef あるいは using
    using uint = unsigned int; // uintという名で使う
    // typedef usigned int uint; //OK
    uint x = 0; // == usigned int x = 0;
    /* メリットは
       1.   本来の名前が長いから短く使いたい、綺麗に使いたい
       2.   宣言される変数の管理をしやすくなる
            例: float a; float b; float c ;
                --> using real = float; real a; real b; real c;
                    後でusing real = double;にする事で今まで宣言したものを綺麗に変更できる*/
    int a_test2 = 10;

    cout << "behind increment before:" << (a_test2++) << endl;
    cout << "after:" << a_test2 << endl;

    cout << "front increment before:" << (++a_test2) << endl;
    cout << "after:" << a_test2 << endl;
    
    /*  operator:
            ? : 条件 式 ? 式: 式 
            * 参照　*式
            & アドレス取る 
            . メンバー選択 オブジェクト.メンバー
            -> メンバー選択 ポインター -> メンバー
            :: スコープ解決 クラス名::メンバー
            :: スコープ解決 名前空間名::名前
            :: グローバル ::名前
    */
    
    return 0;
}
