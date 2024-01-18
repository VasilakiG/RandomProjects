import ctypes

if __name__ == "__main__":
    # Sample data for your call
    x = 6

    clibrary = ctypes.CDLL("./Libraries/pointer.so")

    clibrary.ProducePointer.restype = ctypes.POINTER(ctypes.c_int)
    pointer = clibrary.ProducePointer(ctypes.c_int(x))
    clibrary.ConsumePointer(pointer)

    size = 3

    clibrary.ConsumePointerOfPointers.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))
    pointerArray = (ctypes.POINTER(ctypes.c_int) * size)()

    for i in range(size):
        pointerArray[i] = clibrary.ProducePointer(ctypes.c_int(x))

    clibrary.ConsumePointerOfPointers(pointerArray, ctypes.c_int(size))

    for i in range(size):
        if pointerArray[i] is not None:
            clibrary.free(pointerArray[i])