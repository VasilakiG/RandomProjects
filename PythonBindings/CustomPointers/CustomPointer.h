//
// Created by vasilaki on 18.1.24.
//

#pragma once

#define INSUFFICIENT_SIZE -2
#define FAILURE -1
#define SUCCESS 0

typedef struct {
    int value1;
    int value2;
} CustomPointer;

// Define your data structure to store key-value pairs
struct KeyValue {
    const char *key;
    const char *value;
};

CustomPointer* ProduceCustomPointer(int value1, int value2);
void ConsumeCustomPointer(CustomPointer* ptr);
void ConsumeCustomPointerOfPointers(CustomPointer** ptr_array, int size);

int CP_GetOption(char *key, char *buffer, int *size);
