//
// Created by vasilaki on 5.2.24.
//

#include "EventCounter.hpp"

extern "C" {
    void EventCounter(void* referenceCounter)
    {
        int *eventCounter = static_cast<int*>(referenceCounter);
        *eventCounter += 1;

        std::cout << "Event #" << *eventCounter << std::endl;
    }
}