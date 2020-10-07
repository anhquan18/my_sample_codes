#include<iostream>
#include<vector>
#include<algorithm>


int main(void) 
{
    std::vector<int> vec {1, 20, 5, 6, 7, 10, 4};

    // Use algorithm library with vector
    std::cout << "All members:" << std::endl;
    for (auto &num : vec)
        printf("%d, ", num);
    std::cout << std::endl << std::endl;

    // find function to find a member
    int find_num = 5;
    auto itr = std::find(vec.begin(), vec.end(), find_num);

    if (itr != vec.end()) {
        printf("found %d\n", find_num);
    }
    else {
        printf("didn't find %d\n", find_num);
    }

    // sort function to sort member of list
    std::sort(vec.begin(), vec.end());

    std::cout << "All members after sorted:" << std::endl;
    for (auto &num : vec)
        printf("%d, ", num);
    std::cout << std::endl << std::endl;

    return 0;
}
