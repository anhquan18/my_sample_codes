#include<iostream>
#include<time.h>
#include<vector>

float sumVector_val(const std::vector<float>);
float sumVector_addr(const std::vector<float>&);


int main()
{
    float num1, num2;
    time_t start_time, end_time;
    clock_t start_t;
    std::vector<float> numbers(1000000000, 3.0);
    std::vector<float> *vect_pointer = &numbers;

    // vector and time value as argument
    start_time = time(NULL);
    start_t = clock();
    sumVector_val(numbers);

    std::cout << "Time value:" << time(NULL) - start_time << std::endl;
    std::cout << "Time value:" << (float)(clock() - start_t)/CLOCKS_PER_SEC << "secs" << std::endl;

    // address as argument referrence
    time(&start_time);
    start_t = clock();
    sumVector_addr(numbers);
    time(&end_time);

    std::cout << "Time referrence:" << end_time - start_time << std::endl;
    std::cout << "Time referrence:" << (float)(clock() - start_t)/CLOCKS_PER_SEC << "secs" << std::endl;

    return 0;
}


float sumVector_val(const std::vector<float> numbers)
{
    float sum_value = 0.0;
    for (auto &val: numbers)
        sum_value += val;
    return sum_value;
}


float sumVector_addr(const std::vector<float> &numbers)
{
    float sum_value = 0.0;
    for (auto &val: numbers)
        sum_value += val;
    return sum_value;
}
