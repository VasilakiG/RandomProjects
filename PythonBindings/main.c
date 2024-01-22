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

    printf("=========Testing ClassicPointers:=========\n");
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

    printf("=========Testing CustomPointers:=========\n");
    // Use CustomPointerProducer to get a new custom pointer
    CustomPointer* producedCustomPtr = ProduceCustomPointer(value, value);
    if (producedCustomPtr != NULL) {
        // Use CustomPointerConsumer to consume the custom pointer
        ConsumeCustomPointer(producedCustomPtr);
        free(producedCustomPtr);
    }

    // Create an array of pointers for PointerOfPointersConsumer
    CustomPointer* customPointerArray[size];
    for (int i = 0; i < size; ++i) {
        customPointerArray[i] = ProduceCustomPointer(value, value); // Producing pointers and storing them in the array
    }

    // Use CustomPointerOfPointersConsumer to consume the array of pointers
    ConsumeCustomPointerOfPointers(customPointerArray, size);

    // Freeing the pointers created for the customPointerArray
    for (int i = 0; i < size; ++i) {
        if (customPointerArray[i] != NULL) {
            free(customPointerArray[i]);
        }
    }

    return 0;
}
