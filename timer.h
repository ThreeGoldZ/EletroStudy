#ifndef TIMER_H
#define TIMER_H


#include <cstdlib>
#include <conio.h>
#include <iostream>
#include <stdio.h>
#include <windows.h>
#include <time.h>
#include <math.h>
#include <fstream>
#include <thread>
#include <mutex>
#include <string>
#include <vector>
#include <stdlib.h>
#include <cstdio>
#include <cassert>



class TIMER
{
public:
    TIMER();
    void reset();

    /// seconds() returns the number of seconds (to very high resolution)
    /// elapsed since the timer was last created or reset().
    double seconds();

    /// seconds() returns the number of milliseconds (to very high resolution)
    /// elapsed since the timer was last created or reset().
    double milliseconds();
private:
    double freq_;
    unsigned __int64 baseTime_;
};

#endif // TIMER_H
