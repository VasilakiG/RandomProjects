//
// Created by vasilaki on 18.1.24.
//

#include "CustomPointer.h"

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

CustomPointer* ProduceCustomPointer(const int value1, const int value2)
{
    CustomPointer* ptr = malloc(sizeof(CustomPointer));
    if (ptr != NULL)
    {
        ptr->value1 = value1; // Initialize value1 (you can set it to your desired value)
        ptr->value2 = value2; // Initialize value2 (you can set it to your desired value)
    }
    return ptr;
}

void ConsumeCustomPointer(CustomPointer* ptr)
{
    if (ptr != NULL)
    {
        ptr->value1 = 10; // Set value1 to 10
        ptr->value2 = 20; // Set value2 to 20

        printf("(c)Value1: %d\n", ptr->value1);
        printf("(c)Value2: %d\n", ptr->value2);
    }
}

void ConsumeCustomPointerOfPointers(CustomPointer** ptr_array, const int size)
{
    for (int i = 0; i < size; i++)
    {
        if (ptr_array[i] != NULL)
        {
            printf("(c)Value1 of ptr_array[%d]: %d\n", i, ptr_array[i]->value1);
            printf("(c)Value2 of ptr_array[%d]: %d\n", i, ptr_array[i]->value2);
        }
    }
}

struct KeyValue configOptions[] =
{
    { "option1", "value1" },
    { "option2", "value2" },
};

int CP_GetOption(char *key, char *buffer, int *size)
{
    // Loop through the configuration options to find the key
    for (int i = 0; i < sizeof(configOptions) / sizeof(configOptions[0]); i++)
    {
        if (strncmp(configOptions[i].key, key, sizeof(key)) == 0)
        {
            const char *value = configOptions[i].value;

            if (buffer != NULL && *size > 0)
            {
                // Check if the buffer size is sufficient
                const int len = strlen(value);
                if (*size >= len + 1)
                {
                    // Copy the value to the buffer
                    strcpy(buffer, value);
                    // Update the size to the actual length of the value
                    *size = len;
                }
                else
                {
                    // Buffer size is insufficient
                    return INSUFFICIENT_SIZE;
                }
            }
            else
            {
                // Return the size of the value
                *size = strlen(value) + 1;
                return size[0];
            }
            return SUCCESS; // Key found
        }
    }

    // Key not found
    return FAILURE;
}
