//
// Created by vasilaki on 17.1.24.
//

#include "Pointer.h"

#include <stdlib.h>
#include <stdio.h>

int* ProducePointer(int value) {
    int* ptr = malloc(sizeof(int));
    if (ptr != NULL) {
        *ptr = value; // Assign a value to where ptr is pointing
    }
    return ptr;
}

void ConsumePointer(int* ptr) {
    if (ptr != NULL) {
        printf("Value pointed to by ptr: %d\n", *ptr);
    }
}

void ConsumePointerOfPointers(int** ptr_array, const int size) {
    for (int i = 0; i < size; i++) {
        if (ptr_array[i] != NULL) {
            printf("Value pointed to by ptr_array[%d]: %d\n", i, *ptr_array[i]);
        }
    }
}