//
// Created by root on 18.1.24.
//

#pragma once

typedef struct {
    int value1;
    int value2;
} CustomPointer;

CustomPointer* ProduceCustomPointer(int value1, int value2);
void ConsumeCustomPointer(CustomPointer* ptr);
void ConsumeCustomPointerOfPointers(CustomPointer** ptr_array, int size);