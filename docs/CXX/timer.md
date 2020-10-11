# 三种计时方法

- [1. time_t](#1-time_t)
- [2. clock_t](#2-clock_t)
- [3. gettimeofday](#3-gettimeofday)

## 1. time_t

time_t 计时精确秒，就是相当于获取当时的时间

```c++
#include <time.h>
time_t t;
struct tm *timeinfo;
time(&t);
timeinfo = localtime(&t);
printf("%s", asctime(timeinfo));
```

## 2. clock_t

clock_t 获取的是进程调用 CPU 的时间，多核情况下不准确

```c++
#include <time.h>
clock_t start, finish;
start = clock();
finish = clock();
printf("main: %f ms\n", ((double)(finish - start) / 1000));
```

## 3. gettimeofday

这种方式可以精确到微秒获取程序运行耗费的时间

```c++
#include <sys/time.h>
struct timeval start, end;
gettimeofday(&start, NULL);
gettimeofday(&end1, NULL);
double timeuse = (double)(1000000 * (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec)) / 1000;
printf("%f\n", timeuse); // ms
```
