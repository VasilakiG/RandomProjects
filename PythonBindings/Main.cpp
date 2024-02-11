//
// Created by vasilaki on 5.2.24.
//

#include "EventCounter.hpp"
#include <iostream>

int main()
{
    std::cout << "=========Testing CastingOfPointers:=========" << std::endl;

    std::cout << "Initializing void pointer..." << std::endl;
    void* referenceCounter = new int(1);
    std::cout << "-Done!" << std::endl;

    std::cout << "Calling the EventCounter function" << std::endl;
    EventCounter(referenceCounter);
    std::cout << "-Done!" << std::endl;

    std::cout << "Freeing the void pointer..." << std::endl;
    free(referenceCounter);
    std::cout << "-Done!" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    std::cout << "END OF TESTS" << std::endl;
    std::cout << "=====================================================" << std::endl;

    return 0;
}