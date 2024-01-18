//
// Created by root on 17.1.24.
//

#include <stdio.h>
#include <stdlib.h>

#include "Pointer.h"
#include "CustomPointer.h"

int main() {

    int value;
    printf("Insert a value for the pointer: ");
    scanf("%d", &value);

    // Use PointerProducer to get a new pointer
    int* producedPtr = ProducePointer(value);
    if (producedPtr != NULL) {
        // Use PointerConsumer to consume the pointer
        ConsumePointer(producedPtr);
    }

    // Create an array of pointers for PointerOfPointersConsumer
    const int size = 3;
    int* pointerArray[size];
    for (int i = 0; i < size; ++i) {
        pointerArray[i] = ProducePointer(value); // Producing pointers and storing them in the array
    }

    // Use PointerOfPointersConsumer to consume the array of pointers
    ConsumePointerOfPointers(pointerArray, size);

    // Freeing the pointers created for the pointerArray
    for (int i = 0; i < size; ++i) {
        if (pointerArray[i] != NULL) {
            free(pointerArray[i]);
        }
    }

    return 0;
}
