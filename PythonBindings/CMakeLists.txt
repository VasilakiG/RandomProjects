cmake_minimum_required(VERSION 3.27)

project(PointerProject)

add_subdirectory(ClassicPointers)
add_subdirectory(CustomPointers)
add_subdirectory(EventCounter)

add_executable(PointerProject main.c)
add_executable(CppDemo Main.cpp)

# Link the libraries to the executable
target_link_libraries(PointerProject PRIVATE PointerLib CustomPointerLib)
target_link_libraries(CppDemo PRIVATE EventCounterLib)
