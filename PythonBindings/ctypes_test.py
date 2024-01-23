import ctypes


class CustomPointer(ctypes.Structure):
    pass


CustomPointer._fields_ = [("value1", ctypes.c_int),
                          ("value2", ctypes.c_int)]

if __name__ == "__main__":
    # Sample data to be used
    value = 6
    # Size of the array of pointers
    size = 3

    # Load the shared library into ctypes
    classicPointers = ctypes.CDLL("./Libraries/classicPointers.so")

    # Set the return type of the function to int*
    classicPointers.ProducePointer.restype = ctypes.POINTER(ctypes.c_int)
    # Produce the pointer
    pointer = classicPointers.ProducePointer(ctypes.c_int(value))
    # Consume the produced pointer
    classicPointers.ConsumePointer(pointer)
    # Free the pointer
    classicPointers.free(pointer)

    # Set the return type of the function, None is the equivalent of void
    classicPointers.ConsumePointerOfPointers.restype = None
    # Create an array of pointers of the specified size
    pointerArray = (ctypes.POINTER(ctypes.c_int) * size)()

    # Produce the pointers
    for i in range(size):
        pointerArray[i] = classicPointers.ProducePointer(ctypes.c_int(value))

    # Consume the array of pointers
    classicPointers.ConsumePointerOfPointers(pointerArray, ctypes.c_int(size))

    # Free the pointers
    for i in range(size):
        if pointerArray[i] is not None:  # Check if the pointer is not null
            classicPointers.free(pointerArray[i])

    print("=====================================================")
    print("Test if we can produce custom pointer using Python Bindings")
    print("=====================================================")

    print("-Loading the shared library into ctypes...")
    # Load the shared library into ctypes
    customPointers = ctypes.CDLL("./Libraries/customPointers.so")
    print("-Done!")

    # Set the return type of the function to CustomPointer*
    customPointers.ProduceCustomPointer.restype = ctypes.POINTER(CustomPointer)

    print("-Producing the CustomPointer using Python Bindings...")
    # Produce the pointer
    customPointer = customPointers.ProduceCustomPointer(ctypes.c_int(value), ctypes.c_int(value))
    print("-Done!")

    print("-Consuming the CustomPointer using Python Bindings...")
    # Consume the produced pointer
    customPointers.ConsumeCustomPointer(customPointer)
    print("-Done!")

    print("-Reading the changed values of the CustomPointer from Python...")
    print("(python)Value1 of single CustomPointer: ", customPointer.contents.value1)
    print("(python)Value2 of single CustomPointer: ", customPointer.contents.value2)
    print("-Done!")

    print("-Freeing the memory of the pointer using Python Bindings...")
    # Free the pointer
    customPointers.free(customPointer)
    print("-Done!")

    print("=====================================================")
    print("Test if we can produce custom pointer array using Python Bindings")
    print("=====================================================")

    # Set the return type of the function, None is the equivalent of void
    customPointers.ConsumeCustomPointerOfPointers.restype = None
    # Create an array of pointers of the specified size
    customPointerArray = (ctypes.POINTER(CustomPointer) * size)()

    print("-Producing the array of CustomPointers using Python Bindings...")
    # Produce the pointers
    for i in range(size):
        customPointerArray[i] = customPointers.ProduceCustomPointer(ctypes.c_int(value), ctypes.c_int(value))
        # Test if we can set values from Python and read them in C
        if i == 1:
            print("-Setting the values of the second element of the array from Python...")
            customPointerArray[i].contents.value1 = ctypes.c_int(value * 2)
            customPointerArray[i].contents.value2 = ctypes.c_int(value * 3)
            print("-Done!")
    print("-Done!")

    print("-Consuming the first element of the array of CustomPointers using Python Bindings...")
    customPointers.ConsumeCustomPointer(customPointerArray[0])
    print("-Done!")

    print("-Reading the changed values of the first element of the array of CustomPointers from Python...")
    print("(python)Value1 of the first element of the array: ", customPointerArray[0].contents.value1)
    print("(python)Value2 of the first element of the array: ", customPointerArray[0].contents.value2)
    print("-Done!")

    print("-Consuming the array of CustomPointers using Python Bindings...")
    # Consume the array of pointers
    customPointers.ConsumeCustomPointerOfPointers(customPointerArray, ctypes.c_int(size))
    print("-Done!")

    print("-Freeing the allocated memory of the array of pointers using Python Bindings...")
    # Free the pointers
    for i in range(size):
        if customPointerArray[i] is not None:  # Check if the pointer is not null
            customPointers.free(customPointerArray[i])
    print("-Done!")

    print("=====================================================")
    print("Test if we can create a custom pointer from Python and consume it in C")
    print("=====================================================")

    print("-Creating an instance of CustomPointer from Python class...")
    # Create an instance of CustomPointer
    customPointerInstance = CustomPointer(3, 8)
    print("-Done!")

    print("-Printing the values from the instance of CustomPointer from Python...")
    # Print the values of the instance
    print("CustomPointer instance: " + str(customPointerInstance.value1) + ", " + str(customPointerInstance.value2))
    print("-Done!")

    print("-Passing the instance of CustomPointer created from Python to C and consuming it using Python Bindings...")
    # Consume the instance by passing it by reference
    customPointers.ConsumeCustomPointer(ctypes.byref(customPointerInstance))
    print("-Done!")

    print("=====================================================")
    print("END OF TESTS")
    print("=====================================================")

