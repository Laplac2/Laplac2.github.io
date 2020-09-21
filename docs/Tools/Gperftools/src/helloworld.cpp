#include <iostream>
// #include <gperftools/profiler.h>

using namespace std;

int main()
{
    // ProfilerStart("/tmp/profile");
    cout << "Hello World!" << endl;
    int i = 1000000;

    string *str = new string;
    do
    {
        i--;
    } while (i);
    // ProfilerStop();
    return 0;
}
