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
    print("Test of the buffer behaviour of the GetOption function")
    print("=====================================================")

    INSUFFICIENT_SIZE   = -2
    SUCCESS             =  0

    customPointers.CP_GetOption.restype = ctypes.c_int

    key = ctypes.create_string_buffer(b"option2")
    bufferSize = ctypes.c_int(256)
    buffer = ctypes.create_string_buffer(bufferSize.value)

    #buffer = None

    if buffer is None:
        result = customPointers.CP_GetOption(ctypes.pointer(key), buffer, ctypes.pointer(bufferSize))
    else:
        result = customPointers.CP_GetOption(ctypes.pointer(key), ctypes.pointer(buffer), ctypes.pointer(bufferSize))

    if result == SUCCESS:
        print("Value of", key.value.decode('UTF-8'), "is:", buffer.value.decode('UTF-8'))
    elif result == INSUFFICIENT_SIZE:
        print("Size is too small\n")
    elif result > SUCCESS:
        print("Size is ", result)
    else:
        print("Option not found, ", result)

    print("=====================================================")
    print("Test if ptr can be filled with data from C and read in Python")
    print("=====================================================")

    customPointers.FillCustomPointerOfPointers.restype = None
    # customPointers.FillCustomPointerOfPointers.argtypes = [ctypes.POINTER(CustomPointer),
    #                                                        ctypes.c_int]
    ptr_array = (ctypes.POINTER(ctypes.POINTER(CustomPointer)) * 1)()

    customPointers.FillCustomPointerOfPointers(ptr_array, ctypes.c_int(size))

    # for i in range(size):
    #     print("Value1 of the element of the array: ", ptr_array[i].contents.contents.value1)
    #     print("Value2 of the element of the array: ", ptr_array[i].contents.contents.value2)
    customPointers.ConsumeCustomPointerOfPointers(*ptr_array, ctypes.c_int(size))

    # Free the pointers
    for i in range(len(ptr_array)):
        if ptr_array[i] is not None:  # Check if the pointer is not null
            for j in range(size):
                if ptr_array[i][j] is not None:
                    customPointers.free(ptr_array[i][j])
            customPointers.free(ptr_array[i])

    print("=====================================================")
    print("Test of pointer casting inside C++")
    print("=====================================================")

    pointerCasting = ctypes.CDLL("./Libraries/pointerCasting.so")

    print("Initializing void pointer...")
    referenceCounter = ctypes.c_void_p()
    referenceCounter.value = 1
    print("Done!")

    print("Calling the EventCounter function")
    pointerCasting.EventCounter.restype = None

    pointerCasting.EventCounter(ctypes.byref(referenceCounter))
    print("Done!")

    print("=====================================================")
    print("Test of pointer casting inside Python")
    print("=====================================================")

    def PointerCasting(refCounter) -> None:
        print("Casting the void pointer to int pointer...")
        eventCounter = ctypes.cast(refCounter, ctypes.POINTER(ctypes.c_int))
        print("Done!")
        eventCounter.contents.value += 1
        print(f"Event #{eventCounter.contents.value}")


    PointerCasting(ctypes.byref(referenceCounter))

    print("=====================================================")
    print("END OF TESTS")
    print("=====================================================")
