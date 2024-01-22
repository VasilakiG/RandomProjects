//
// Created by root on 18.1.24.
//

#include "CustomPointer.h"

#include <stdlib.h>
#include <stdio.h>

CustomPointer* ProduceCustomPointer(const int value1, const int value2) {
    CustomPointer* ptr = (CustomPointer*)malloc(sizeof(CustomPointer));
    if (ptr != NULL) {
        ptr->value1 = value1; // Initialize value1 (you can set it to your desired value)
        ptr->value2 = value2; // Initialize value2 (you can set it to your desired value)
    }
    return ptr;
}

void ConsumeCustomPointer(CustomPointer* ptr) {
    if (ptr != NULL) {

        ptr->value1 = 10; // Set value1 to 10
        ptr->value2 = 20; // Set value2 to 20

        printf("(c)Value1: %d\n", ptr->value1);
        printf("(c)Value2: %d\n", ptr->value2);
    }
}

void ConsumeCustomPointerOfPointers(CustomPointer** ptr_array, const int size) {
    for (int i = 0; i < size; i++) {
        if (ptr_array[i] != NULL) {
            printf("(c)Value1 of ptr_array[%d]: %d\n", i, ptr_array[i]->value1);
            printf("(c)Value2 of ptr_array[%d]: %d\n", i, ptr_array[i]->value2);
        }
    }
}
