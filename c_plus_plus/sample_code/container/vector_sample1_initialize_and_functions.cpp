#include<iostream>
#include<vector>
using namespace std;

/*
 参考のURL:
http://vivi.dyndns.org/tech/cpp/vector.html#vec-assign
 */

// A better options for making arrays
// an array with size can be changed

int main()
{
    vector<int> vect1;
    vector<double> vect2 {1.,2.,3.};
    vector<double> vect3(10, 1.0);
    vector<int> vect4;
    vector<int> vect5;
    vector< vector<double> > multi_dimensions_vect;// 2 Dimension arrays
    vector< vector<double> > multi_dimensions_vect1(3, vector<double>(3)); // initialize vector size
    vector< vector<double> > multi_dimensions_vect2(3, vector<double>(3, 1.0)); // initialize vector size with same default value
    vector< vector<double> > multi_dimensions_vect3 { {2.0,3.0}, {1.0,2.0,3.0}}; // initlize vector with diffirent values
    vector<vector<vector<double>>> tri_dimension_vect;


    // Loop 1 like normal array
    cout << "Loop 1: normal for" << endl;
    for (int i=0; i < vect2.size(); i++)
        printf("%lf, ", vect2[i]);
    cout << endl << endl;

    // Loop 2 use "for" to access all member of vector (python?)
    cout << "Loop 2: python like? for" << endl;
    for (auto &num: vect2)
        printf("%lf, ", num);
    cout << endl << endl;

    // Loop 3 use iterator pointer 
    // iterator intialize:
    // vector<double>::iterator itr; *itr; to referrence value;
    // ++itr; --itr; to move pointer to the next or previous member
    // vector.begin() will return the iterator of the head member
    // vector.end() will return the iterator of the last member
    cout << "Loop 3: iterator pointer" << endl;
    for (auto itr = vect2.begin(); itr != vect2.end(); ++itr)
        printf("%lf, ", *itr);
    cout << endl << endl;

    //***********************************************************
    // Functions of vector
    // vector.push_back(), vector.emplace_back() add a member at the end of an array
    vect1.push_back(4.);
    vect1.emplace_back(5.);

    // vector.insert(iterator, value), vector.emplace() add a member to the head or a position of an array 
    vect1.insert(vect1.begin(), 7);
    vect1.insert(vect1.begin()+2, 8);
    vect1.emplace(vect1.end()-1, 9);

    cout << "Loop 4: add member" << endl;
    for (auto &num: vect1)
        cout << num << ",";
    cout << endl << endl;

    // vector.pop_back() to delete last member
    vect1.pop_back();

    int num1 = vect1.back(); // last member's value
    cout << num1 << endl;

    // vector.erase(iterator) to delete a member
    vect1.erase(vect1.begin() + 2);

    cout << "Loop 5: after member deleted" << endl;
    for (auto &num: vect1)
        cout << num << ",";
    cout << endl << endl;

    cout << "size of vect1:" << vect1.size() << endl;

    cout << "Loop 6: multidimensions with i and j for" << endl;
    for (int i=0; i<multi_dimensions_vect2.size(); ++i)
        for (int j=0; j<multi_dimensions_vect2[i].size(); ++j)
            cout << multi_dimensions_vect2[i][j] << ",";
    cout << endl << endl;
    
    cout << "Loop 7: multidimensions with python like?" << endl;
    for (auto &num_list : multi_dimensions_vect2)
        for (auto &num : num_list)
            cout << num << ",";
    cout << endl << endl;

    //***********************************************************
    // resize vector
    // create 6x6 dimensions
    
    multi_dimensions_vect2.resize(6);
    for (size_t i=0; i<6; i++)
        multi_dimensions_vect2[i].resize(6);

    multi_dimensions_vect3.resize(5, vector<double>(4));

    cout << "After resized" << endl;
    cout << "vect2:" << multi_dimensions_vect2.size() << endl;
    cout << "vect3:" << multi_dimensions_vect3.size() << endl;
    
    //***********************************************************
    // copy a vector
    // copy with for
    vector<int> copied_vect;
    vector<double> copied_vect2;

    for (size_t i=0; i < vect1.size(); i++)
        copied_vect.push_back(vect1[i]);
    vect1[0] = 10;

    // No connect between old and new vector
    cout << "1First element of old vector is" << vect1[0] << endl;
    cout << "1First element of new vector is" << copied_vect[0] << endl;

    // copy using assignment = operator
    copied_vect2 = vect2;

    // No connect between old and new vector
    vect2[0] = 100.;
    cout << "2First element of old vector is" << vect2[0] << endl;
    cout << "2First element of new vector is" << copied_vect2[0] << endl;

    // Deeply copy vector by passing vector as constructor
    // Declaring new vector and copying element of old vector 
    // constructor method, Deep copy
    vector<double> copied_vect3(vect3);

    // No connect between old and new vector
    vect3[0] = 1000.;
    cout << "3First element of old vector is" << vect3[0] << endl;
    cout << "3First element of new vector is" << copied_vect3[0] << endl;

    // copy using builtin functions
    // copy function
    // copy(first_iterator_want_to_copy, last_iterator_want_to_copy, back_inserter())
    // copy(vect1.begin(), vect1.end(), vect4.begin());
    copy(vect1.begin(), vect1.end(), back_inserter(vect4));

    cout << "4Old vector elements are: ";
    for (auto &num : vect1)
        cout << num << ",";
    cout << endl;

    cout << "4New vector elements are: ";
    for (auto &num : vect4)
        cout << num << ",";
    cout << endl;

    // No connect between old and new vector
    vect1[0] = 10000.;

    cout << "5First element of new vector is" << vect4[0] << endl;

    // assign method also deep copy
    // assign(first_iterator_want_to_copy, last_iterator_want_to_copy)
    vect1.resize(10,3);
    vect5.assign(vect1.begin()+3, vect1.end()-1);
    cout << "1New assigned vector elements are: ";
    for (auto &num : vect5)
        cout << num << ",";
    cout << endl;

    vect5.empty();

    double m_double[] = {1., 5., 19., 26.};

    // assign from array
    vect5.assign(m_double, m_double+20); // no error but 0.0 will be added at the end of the vector

    cout << "2New assigned vector elements are: ";
    for (auto &num : vect5)
        cout << num << ",";
    cout << endl;

    return 0;
}
