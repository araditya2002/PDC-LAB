#include <omp.h>
#include <iostream>
#include <stdlib.h>
using namespace std;
int main()
{
int n_td, tid;
bool offset = true;
#pragma omp parallel private(n_td, tid)
{
tid = omp_get_thread_num();
printf("Thread id: %d\n", tid);

// the if block below makes sure that number of threads is printed exactly once
if (offset)
{
n_td = omp_get_num_threads();

printf("Number of Threads: %d\n", n_td);

offset = false;
}
}
return 0;
}