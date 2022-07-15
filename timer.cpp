#include "timer.h"

TIMER::TIMER()
{
    reset();
}

void TIMER::reset(){
    unsigned __int64 pf;
    QueryPerformanceFrequency((LARGE_INTEGER *)&pf);
    freq_ =1.0/ (double) pf;
    QueryPerformanceCounter((LARGE_INTEGER *)&baseTime_);
}

/// seconds() returns the number of seconds (to very high resolution)
/// elapsed since the timer was last created or reset().
double TIMER::seconds() {
        unsigned __int64 val;
        QueryPerformanceCounter((LARGE_INTEGER *)&val);
        return (val - baseTime_) * freq_;
}

/// seconds() returns the number of milliseconds (to very high resolution)
/// elapsed since the timer was last created or reset().
double TIMER::milliseconds() {
        return seconds() * 1000.0;
}
